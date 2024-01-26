#!/usr/bin/env python

from pyramid import __version__
from pyramid.utils import get_input, log, log_progress, print_final

import sys
import time
import traceback


def process(instr):
    nsteps = 10
    wait = float(instr)

    total = 0

    for i in range(nsteps):
        log_progress({"progress": (i / nsteps)})
        time.sleep(wait)

    print_final({"wait_time": (wait * 10)})


def main():
    timeout = int(sys.argv[-1])

    time.sleep(2)
    log("pyramid process ready - version %s" % __version__)
    to_process = get_input(timeout)

    while to_process and to_process != "terminate":
        log('Processing "%s"' % to_process)

        try:
            process(to_process)
        except:
            print_final({"error": traceback.format_exc()})

        to_process = get_input(timeout)

    log("Terminating...")


if __name__ == "__main__":
    main()
