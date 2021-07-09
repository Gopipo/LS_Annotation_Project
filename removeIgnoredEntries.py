#!/usr/bin/python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import json

def checkAccept(line):
    """
    Loads JSON from string, checks whether to accept the example, returns accept boolean.
    """
    accept = False
    jsonline = json.loads(line)
    if jsonline["answer"] == "accept":
        accept = True
    return accept

def parse_args():
    parser = ArgumentParser(description="State the input and output files.")
    parser.add_argument("-i", "--infile",
                        help="Enter the absolute path to the infile (JSONL-files only).",
                        required=True)
    parser.add_argument("-o", "--outfile",
                        help="Enter the absolute path to the outfile (opened in 'w' mode, writes a JSONL-file).",
                        required=True)
    args = parser.parse_args()
    return args

def main():
    """Deletes skipped images from corpus..
    """
    args = parse_args()
    with open(args.infile, "r", encoding="utf-8") as inf:
        with open(args.outfile, "w", encoding="utf-8") as of:
            for line in inf:
                # line is a full JSON-format
                accept = checkAccept(line)
                if accept:
                    of.write(line)
                    of.write("\n")


if __name__ == "__main__":
    main()
