# Copyright (C) 2021 Matthias Nadig

import os
import argparse

from .._codes import ENCODING_LOGFILES


def main():
    parser = argparse.ArgumentParser(
        prog='Logfiles-Printer',
        description='Prints content of a logfile to command line')

    parser.add_argument('-f', '--file', type=str, required=True, help='Filename of logfile to be printed')
    parser.add_argument('-p', '--prune', type=int, default=0, help='Number of lines to be printed (most-recent)')

    args = parser.parse_args()
    filename = args.file
    n_lines = args.prune

    if not os.path.isfile(filename):
        raise FileNotFoundError(f'"{filename}"')

    with open(filename, 'r', encoding=ENCODING_LOGFILES) as f:
        lines = f.readlines()

    lines = lines[-n_lines:]
    lines = ''.join(lines)

    print(lines)


if __name__ == '__main__':
    main()
