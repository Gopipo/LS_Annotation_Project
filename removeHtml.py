#!/usr/bin/python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

import os
import re


def parse_args():
    parser = ArgumentParser(description="Enter the text file conatining the \
                            output of 'file * > filetypes.txt' and the folder \
                            in which to find it.")
    parser.add_argument("-f", "--folder",
                        help="Enter the absolute path to the image folder \
                              where the filetypes.txt file is and the \
                              html-files should be removed",
                        required=True)
    parser.add_argument("-t", "--txtfile",
                        help="Enter the filename of the file containing the \
                              output of 'file * > filetypes.txt'. Default \
                              = 'filetypes.txt'..",
                        default="filetypes.txt")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    filepath = os.path.join(args.folder, args.txtfile)
    with open(filepath, "r", encoding="utf-8") as inf:
        for line in inf:
            match = re.match(r"^(\d+_([LAS]{2}_)?\d+(.+)?): +(.{4})", line)
            filename = match[1]
            # filetype will contain whitespaces if len(filetype<4)
            filetype = match[4]
            if filetype == "HTML":
                filename = os.path.join(args.folder, filename)
                os.remove(filename)


if __name__ == "__main__":
    main()
