#!/usr/bin/env python3
import argparse
import pathlib
import sys

from read_time.read_time import ReadTime


def main():
    # Code goes here
    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--loglevel",
        dest="log_level",
        default="INFO",
        help="log level to use, default [INFO], options [INFO, DEBUG, ERROR]",
    )
    args = vars(parser.parse_args())
    # Code goes here

if __name__ == "__main__":
    main()
