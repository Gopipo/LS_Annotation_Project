#!/usr/bin/python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

import os
import re


def parse_args():
    parser = ArgumentParser(description="Enter the absolute path to the folder \
                            in which to fix image file extensions.")
    parser.add_argument("-f", "--folder",
                        help="Enter the absolute path to the image folder \
                              where to fix image file extensions.",
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    counter = 0
    for filename in os.listdir(args.folder):
        if re.match(r"(.+_\d+)([jpegnsvc+xmlif]{3,7})$", filename):
            newfilename = re.sub(r"(.+_\d+)([jpegnsvc+xmlif]{3,7})$",
                                 r"\1.\2",
                                 filename)
            filename = os.path.join(args.folder, filename)
            newfilename = os.path.join(args.folder, newfilename)
            os.rename(filename, newfilename)
            counter += 1
    answer = "Fixed " + str(counter)
    if counter == 0:
        print("All filenames already correct.")
    else:
        if counter == 1:
            answer += " filename."
        else:
            answer += " filenames."
        print(answer)


if __name__ == "__main__":
    main()
