#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Amanda Simmons, Pete M"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # print(dirname)
    # print(os.path.abspath(dirname))
    # print(os.listdir(dirname))
    abs_paths_list = []
    file_names_list = os.listdir(dirname)
    for f in file_names_list:
        match_object = re.search(r'\w+__\w+__.\w+', f)
        if match_object:
            # abs_paths_list.append(os.path.abspath(match_object.group(0)))
            abs_paths_list.append(os.path.abspath(f))
            for path in abs_paths_list:
                print(path)
                print(f)

    return abs_paths_list

def copy_to(path_list, dest_dir):
    # your code here
    return


def zip_to(path_list, dest_zip):
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='origin directory')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    get_special_paths(ns.from_dir)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.
    # print(ns.from_dir)
    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
