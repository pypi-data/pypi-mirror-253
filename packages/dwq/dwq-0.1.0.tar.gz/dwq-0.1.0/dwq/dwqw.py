#!/usr/bin/env python3

import argparse
import os
import threading
import random
import time
import signal
import socket
import traceback
import multiprocessing
import shutil
from subprocess import run, PIPE, STDOUT, TimeoutExpired, CalledProcessError

import redis
from redis.exceptions import ConnectionError, RedisError

from dwq import Job, Disque

import dwq.cmdserver as cmdserver
from dwq.gitjobdir import GitJobDir

import dwq.util as util

from dwq.version import __version__


def sigterm_handler(signal, stack_frame):
    raise SystemExit()


def parse_args():
    parser = argparse.ArgumentParser(
        prog="dwqw", description="dwq: disque-based work queue (worker)"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )

    parser.add_argument(
        "-q",
        "--queues",
        type=str,
        help='queues to wait for jobs (default: "default")',
        nargs="*",
        default=["default"],
    )
    parser.add_argument(
        "-j",
        "--jobs",
        help="number of workers to start",
        type=int,
        default=multiprocessing.cpu_count(),
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="name of this worker (default: hostname)",
        default=socket.gethostname(),
    )

    parser.add_argument(
        "-D",
        "--disque-url",
        help="specify disque instance [default: localhost:7711]",
        type=str,
        action="store",
        default=os.environ.get("DWQ_DISQUE_URL", "localhost:7711"),
    )

    parser.add_argument(
        "-v", "--verbose", help="be more verbose", action="count", default=1
    )
    parser.add_argument(
        "-Q", "--quiet", help="be less verbose", action="count", default=0
    )

    return parser.parse_args()


shutdown = False

active_event = threading.Event()


def worker(n, cmd_server_pool, gitjobdir, args, working_set):
    global active_event
    global shutdown

    worker_str = f"dwqw@{args.name}.{n}"
    print(f"{worker_str}: started")
    buildnum = 0
    while not shutdown:
        try:
            if not shutdown and not Disque.connected():
                time.sleep(1)
                continue
            while not shutdown:
                active_event.wait()
                jobs = Job.get(args.queues)
                for job in jobs:
                    if shutdown or not active_event.is_set():
                        job.nack()
                        continue

                    if job.additional_deliveries > 2:
                        error = "too many deliveries (usual reason: timeout)"
                        vprint(2, f"{worker_str}: {error}")
                        job.done(
                            {
                                "status": "error",
                                "output": f"{worker_str}: {error}\n",
                                "worker": args.name,
                                "runtime": 0,
                                "body": job.body,
                            }
                        )
                        continue

                    buildnum += 1
                    working_set.add(job.job_id)
                    before = time.time()
                    vprint(
                        2,
                        f"{worker_str}: got job {job.job_id} from queue {job.queue_name}",
                    )

                    try:
                        command = job.body["command"]
                    except KeyError:
                        vprint(2, f"{worker_str}: invalid job json body")
                        job.done(
                            {
                                "status": "error",
                                "output": f'{worker_str} invalid job body: "{job.body}"',
                            }
                        )
                        continue

                    vprint(2, f'{worker_str}: command="{command}"')

                    repo = None
                    commit = None

                    try:
                        repo = job.body["repo"]
                        commit = job.body["commit"]
                    except KeyError:
                        pass

                    if (repo is None) ^ (commit is None):
                        vprint(
                            2,
                            f"{worker_str}: invalid job json body, only one of repo and commit specified",
                        )
                        job.done(
                            {
                                "status": "error",
                                "output": f'{worker_str} invalid job body: "{job.body}"',
                            }
                        )
                        continue

                    exclusive = None
                    try:
                        options = job.body.get("options") or {}
                        if options.get("jobdir") or "" == "exclusive":
                            exclusive = str(random.random())
                    except KeyError:
                        pass

                    unique = random.random()

                    _env = os.environ.copy()

                    try:
                        _env.update(job.body["env"])
                    except KeyError:
                        pass

                    _env.update(
                        {
                            "DWQ_QUEUE": job.queue_name,
                            "DWQ_WORKER": args.name,
                            "DWQ_WORKER_BUILDNUM": str(buildnum),
                            "DWQ_WORKER_THREAD": str(n),
                            "DWQ_JOBID": job.job_id,
                            "DWQ_JOB_UNIQUE": str(unique),
                            "DWQ_CONTROL_QUEUE": job.body.get("control_queues")[0],
                        }
                    )

                    workdir = None
                    workdir_output = None
                    workdir_error = None
                    try:
                        if repo is not None:
                            _env.update(
                                {
                                    "DWQ_REPO": repo,
                                    "DWQ_COMMIT": commit,
                                }
                            )

                            try:
                                (workdir, workdir_output) = gitjobdir.get(
                                    repo, commit, exclusive=exclusive or str(n)
                                )
                            except CalledProcessError as e:
                                workdir_error = (
                                    f"{worker_str}: error getting jobdir. output:\n"
                                    + e.output.decode("utf-8", "backslashreplace")
                                )

                            if not workdir:
                                if job.nacks < options.get("max_retries", 2):
                                    job.nack()
                                    vprint(
                                        1,
                                        f"{worker_str}: error getting job dir, requeueing job",
                                    )
                                    if workdir_error:
                                        vprint(
                                            1,
                                            f'{worker_str}: jobdir error: "{workdir_error}"',
                                        )
                                else:
                                    job.done(
                                        {
                                            "status": "error",
                                            "output": workdir_error
                                            or f"{worker_str}: error getting jobdir\n",
                                            "worker": args.name,
                                            "runtime": 0,
                                            "body": job.body,
                                        }
                                    )
                                    vprint(
                                        1,
                                        f"{worker_str}: cannot get job dir, erroring job",
                                    )
                                working_set.discard(job.job_id)
                                continue
                        else:
                            workdir = "/tmp"

                        workdir_done_at = time.time()
                        files = options.get("files")
                        util.write_files(files, workdir)
                        write_files_done_at = time.time()

                        # assets
                        asset_dir = os.path.join(
                            workdir, "assets", "%s:%s" % (hash(job.job_id), str(unique))
                        )
                        _env.update({"DWQ_ASSETS": asset_dir})

                        timeout = options.get("timeout", 300)

                        # subtract time used for checkout and job files
                        timeout -= time.time() - before

                        # be sure to timeout a bit earlier, so transmit/network delays
                        # don't make disque time-out itself.
                        timeout -= 10

                        command_start_at = time.time()

                        if timeout > 0:
                            try:
                                res = run(
                                    command,
                                    stdout=PIPE,
                                    stderr=STDOUT,
                                    cwd=workdir,
                                    shell=True,
                                    env=_env,
                                    start_new_session=True,
                                    timeout=timeout,
                                )

                                result = res.returncode
                                output = res.stdout.decode("utf-8", "backslashreplace")

                            except TimeoutExpired as e:
                                result = "timeout"
                                decoded = e.output.decode("utf-8", "backslashreplace")
                                output = f"{decoded}{worker_str}: error: timed out\n"

                        else:
                            result = "timeout"
                            output = f"{worker_str}: command timed out while setting up job\n"

                        command_done_at = time.time()

                        if (result not in {0, "0", "pass"}) and job.nacks < options.get(
                            "max_retries", 2
                        ):
                            vprint(
                                2,
                                f"{worker_str}: command:",
                                command,
                                "result:",
                                result,
                                "nacks:",
                                job.nacks,
                                "re-queueing.",
                            )
                            job.nack()
                        else:
                            cmd_runtime = command_done_at - command_start_at
                            workdir_setup_time = workdir_done_at - before
                            write_files_time = write_files_done_at - workdir_done_at

                            options = job.body.get("options")
                            if options:
                                options.pop("files", None)

                            # remove options from body if it is now empty
                            if not options:
                                job.body.pop("options", None)

                            _result = {
                                "status": result,
                                "output": output,
                                "worker": args.name,
                                "body": job.body,
                                "unique": str(unique),
                                "times": {
                                    "cmd_runtime": cmd_runtime,
                                },
                            }

                            if files:
                                _result["times"]["write_files"] = write_files_time

                            if workdir_output:
                                _result["workdir_output"] = workdir_output.decode(
                                    "utf-8", "backslashreplace"
                                )
                                _result["times"]["workdir_setup"] = workdir_setup_time

                            # pack assets
                            try:
                                asset_files = []
                                for subdir, _, subdir_files in os.walk(asset_dir):
                                    # subdir is the absolute folder,
                                    # subdir_files a list of files.
                                    # here, we compile a list of file paths
                                    # relative to asset_dir.
                                    asset_files.extend(
                                        [
                                            os.path.relpath(
                                                os.path.join(subdir, f), asset_dir
                                            )
                                            for f in subdir_files
                                        ]
                                    )

                                if asset_files:
                                    before_assets = time.time()
                                    _result.update(
                                        {
                                            "assets": util.gen_file_data(
                                                asset_files, asset_dir
                                            )
                                        }
                                    )
                                    shutil.rmtree(asset_dir, ignore_errors=True)
                                    _result["times"]["assets"] = (
                                        time.time() - before_assets
                                    )

                            except FileNotFoundError:
                                pass

                            runtime = time.time() - before
                            _result["runtime"] = runtime

                            job.done(_result)

                            vprint(
                                2,
                                f"{worker_str}: command:",
                                command,
                                "result:",
                                result,
                                "runtime: %.1fs" % runtime,
                            )
                            working_set.discard(job.job_id)
                    except Exception as e:
                        if workdir and repo:
                            gitjobdir.release(workdir)
                        raise e

                    if repo:
                        gitjobdir.release(workdir)

        except Exception as e:
            print(f"{worker_str}: uncaught exception")
            traceback.print_exc()
            time.sleep(2)
            print(f"{worker_str}: restarting worker")


class SyncSet(object):
    def __init__(self):
        self.set = set()
        self.lock = threading.Lock()

    def add(self, obj):
        with self.lock:
            self.set.add(obj)

    def discard(self, obj):
        with self.lock:
            self.set.discard(obj)

    def empty(self):
        with self.lock:
            oldset = self.set
            self.set = set()
            return oldset


verbose = 0


def vprint(n, *args, **kwargs):
    global verbose
    if n <= verbose:
        print(*args, **kwargs)


def handle_control_job(args, job):
    global active_event
    global shutdown
    body = job.body
    status = 0
    result = ""

    try:
        control = body["control"]
        cmd = control["cmd"]
        if cmd == "shutdown":
            vprint(1, "dwqw: shutdown command received")
            result = "shutting down"
            shutdown = 1

        elif cmd == "pause":
            if not active_event.is_set():
                vprint(1, "dwqw: pause command received, but already paused")
                result = "already paused"
            else:
                vprint(1, "dwqw: pause command received")
                active_event.clear()
                result = "paused"
        elif cmd == "resume":
            if active_event.is_set():
                vprint(1, "dwqw: resume command received, but not paused")
                result = "not paused"
            else:
                vprint(1, "dwqw: resume command received. resuming ...")
                active_event.set()
                result = "resumed"
        elif cmd == "ping":
            vprint(1, "dwqw: ping received")
            result = "pong"
        else:
            vprint(1, 'dwqw: unknown control command "%s" received' % cmd)

    except KeyError:
        vprint(1, "dwqw: error: invalid control job")

    control_reply(args, job, result, status)

    if shutdown:
        raise SystemExit()


def control_reply(args, job, reply, status=0):
    job.done({"status": status, "output": reply, "worker": args.name, "body": job.body})


def main():
    global shutdown
    global verbose
    global active_event

    args = parse_args()
    verbose = args.verbose - args.quiet

    cmd_server_pool = cmdserver.CmdServerPool(args.jobs)

    signal.signal(signal.SIGTERM, sigterm_handler)

    _dir = "/tmp/dwq.%s" % str(random.random())
    gitjobdir = GitJobDir(_dir, args.jobs)

    servers = [args.disque_url]
    try:
        Disque.connect(servers)
        vprint(1, "dwqw: connected.")
    except:
        pass

    working_set = SyncSet()

    for n in range(1, args.jobs + 1):
        threading.Thread(
            target=worker,
            args=(n, cmd_server_pool, gitjobdir, args, working_set),
            daemon=True,
        ).start()

    active_event.set()

    try:
        while True:
            if not Disque.connected():
                try:
                    vprint(1, "dwqw: connecting...")
                    Disque.connect(servers)
                    vprint(1, "dwqw: connected.")
                except RedisError:
                    time.sleep(1)
                    continue

            try:
                control_jobs = Job.get(["control::worker::%s" % args.name])
                for job in control_jobs or []:
                    handle_control_job(args, job)
            except RedisError:
                pass

    except (KeyboardInterrupt, SystemExit):
        vprint(1, "dwqw: shutting down")
        shutdown = True
        cmd_server_pool.destroy()
        vprint(1, "dwqw: nack'ing jobs")
        jobs = working_set.empty()
        d = Disque.get()
        d.nack_job(*jobs)
        vprint(1, "dwqw: cleaning up job directories")
        gitjobdir.cleanup()
