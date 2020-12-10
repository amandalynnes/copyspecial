#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Amanda Simmons, Pete M, Ana Ruiz, Drew S, Kano, Daniel"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""

    abs_paths_list = []
    file_names_list = os.listdir(dirname)
    for f in file_names_list:
        match_object = re.search(r'__\w+__', f)
        if match_object:
            file_path = os.path.join(dirname, f)
            abs_paths_list.append(os.path.abspath(file_path))

    return abs_paths_list


def copy_to(path_list, dest_dir):
    """Given path_list and dest_dir,
    it makes any subdirectories/ directories needed."""
    os.makedirs(dest_dir)
    for f in path_list:
        shutil.copy(f, dest_dir)

    return


def zip_to(path_list, dest_zip):
    """Given path_list and dest_dir,
    it makes any subdirectories/ directories needed."""
    subprocess.run(['zip', '-j', dest_zip] + path_list)
    # print(subprocess.run(zip -j dest_zip path_list))
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
    from_dir = ns.from_dir
    specials_paths_list = get_special_paths(from_dir)
    to_dir = ns.todir
    to_zip = ns.tozip

    if to_dir:
        copy_to(specials_paths_list, to_dir)
    elif to_zip:
        zip_to(specials_paths_list, to_zip)
    else:
        for path in specials_paths_list:
            print(path)
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
