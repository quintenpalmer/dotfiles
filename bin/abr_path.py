#!/usr/bin/env python
import sys
import re
import os


def shorten_single(directory):
    return directory[0] if directory else directory


def shorted_leading(directory_list):
    return list(map(shorten_single, directory_list[:-1])) + [directory_list[-1]]


def shorten_path(full_path):
    return '/'.join(shorted_leading(full_path.split('/')))


def pretty_path(full_path):
    full_path = re.sub('/home/\w+', '~', full_path)
    return shorten_path(full_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        path = os.getcwd()
    else:
        path = sys.argv[1]
    print(pretty_path(path))
