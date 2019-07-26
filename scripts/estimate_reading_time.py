#!/usr/bin/env python3
import argparse

from read_time.read_time import ReadTime


def main():
    parser = argparse.ArgumentParser(
        description="Guesstimate the time it will take to finish reading a post"
    )
    parser.add_argument(
        "--url", "-u", required=True, dest="url", help="URL containing text."
    )
    parser.add_argument(
        "--loglevel",
        dest="log_level",
        default="INFO",
        help="log level to use, default [INFO], options [INFO, DEBUG, ERROR]",
    )
    args = vars(parser.parse_args())
    read_time = ReadTime(args.get("url"), args.get("log_level"))
    guestimate = read_time.estimate_reading_time()
    print(f"{guestimate} Min Read")


if __name__ == "__main__":
    main()
