#!/usr/bin/env python3

import json
import random
import os
import signal
import sys
import time
import argparse
import subprocess

from dwq import Job, Disque
import dwq.util as util

from dwq.version import __version__


def sigterm_handler(signal, stack_frame):
    raise SystemExit()


def parse_args():
    parser = argparse.ArgumentParser(
        prog="dwq-localjob", description="dwq: disque-based work queue"
    )

    parser.add_argument(
        "-D", "--disque-url", help="specify disque instance [default: localhost:7711]",
        type=str, action="store", default=os.environ.get("DWQ_DISQUE_URL", "localhost:7711"),
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )

    parser.add_argument("command", type=str, nargs="1+")

    return parser.parse_args()


def vprint(*args, **kwargs):
    global verbose
    if verbose:
        print(*args, **kwargs)


verbose = False


def main():
    global verbose
    args = parse_args()

    try:
        control_queue = os.environ["DWQ_CONTROL_QUEUE"]
    except KeyError:
        print("dwqc: error: DWQ_CONTROL_QUEUE unset.")
        sys.exit(1)

    try:
        parent_jobid = os.environ["DWQ_JOBID"]
    except KeyError:
        print("dwqc: error: DWQ_JOBID unset.")
        sys.exit(1)

    verbose = args.verbose
    signal.signal(signal.SIGTERM, sigterm_handler)
    Disque.connect([args.disque_url])

    result = subprocess.run(args.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)
