#!/usr/bin/env python3
import argparse
from gendiff.diff_calculation import generate_diff


def main():
    desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
