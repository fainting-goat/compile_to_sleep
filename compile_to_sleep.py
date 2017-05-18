#!/usr/bin/env python
"""
NAME
    compile_to_sleep - help Kelsey sleep

SYNOPSIS
    template [-h] [-f file] [-s speed]
"""

import argparse
import os
import sys
import time
import traceback


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Help Kelsey sleep")
    parser.add_argument("-f", dest="file", default="default.txt",
        help="text file to traverse")
    parser.add_argument("-s", dest="speed", default=0.7,
        help="lines per second")
    return parser.parse_args()


def main():
    try:
        args = parse_args()

        contents = []
        with open(args.file) as f:
            for line in f:
                contents.append(line)

        while True:
            for line in contents:
                print(line.rstrip())
                time.sleep(float(args.speed))

    except Exception as e:
        print(str(e) + "\n")
        traceback.print_exc()
        os._exit(1)


if __name__ == '__main__':
    main()