#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
import argparse


# @CHECK_PATH
imageDirectory = "./Corpora/images_webcorpus/"
# text directory without "monolingual" or "parallel"
textDirectory = "./Corpora/tokenized_txt_files/tokenized_"
targetDir = "./Corpora/JSON/"
targetFile = "imageTextPaired.jsonl"
mode = ""


def parse_args():
    parser = argparse.ArgumentParser(description="You may specify source \
        directories for images and texts, and the outfile (JSONL Format)")
    parser.add_argument("-i", "--imgdir",
                        type=str,
                        help="path of top most image directory",
                        default=imageDirectory,
                        required=False)
    parser.add_argument("-t", "--txtdir",
                        type=str,
                        help="path of top most text directory",
                        default=textDirectory,
                        required=False)
    parser.add_argument("-o", "--outfile",
                        type=str,
                        help="name of outfile (JSONL format)",
                        default=targetFile,
                        required=False)
    args = parser.parse_args()
    return args


def getMode(path) -> str:
    """ Pre: file structure is thus that directory containing parallel or
    monolingual text files is marked as such. "_parallel" or "_monolingual"
    must be the end of the directory name.

    Checks whether loop currently is in a parallel or monolingual directory
    and sets mode to the corresponding option..
    """
    currentMode = re.findall("_([A-Za-z0-9]+)$", path)
    return currentMode[0]


def writeJSON(imagePath, textPath, outfile):
    """ Appends JSON Lines file with image path and text to be fed to prodigy
    as stream for annotation.
    """
    # read txt file content
    content = ""
    with open(textPath, "r", encoding="utf-8") as sf:
        for line in sf:
            content = content + line

    # create JSON format
    dict = {"image": imagePath, "text": content}
    # append file
    with open(outfile, "a", encoding="utf-8") as f:
        json.dump(dict, f)
        f.write("\n")


def check_fileExists(outfile):
    """Alert user if .jsonl file already exists."""
    if os.path.isfile(outfile):
        appendVerification = ""
        while appendVerification != "y" and appendVerification != "n":
            appendVerification = input("The file\
             ./Corpora/JSON/imageTextPaired.jsonl already exists.\
              \n Are you sure you want to append said file with the data in:\
               ./Corpora/images_webcorpus/ \n (y/n): ")
        if appendVerification == "n":
            sys.exit("Execution stopped.")


def main():
    """Pre: Only execute this once. Appends imageTextPaired.jsonl file!
    Exception: completely new set of image data in the given directories.

    Crawls through all image directories, pairs up the image path with the
    corresponding text, appends the pair to the specified .jsonl
    file..
    """
    args = parse_args()
    outfilePath = targetDir + args.outfile
    check_fileExists(outfilePath)

    # @CHECK_STRUCTURE
    # images_html/, images_pdf/
    for subdirectory0 in os.listdir(args.imgdir):
        subdirectory0 += "/"
        # */*_monolingual/, */*_parallel/
        for subdirectory1 in os.listdir(args.imgdir
                                        + subdirectory0):
            mode = getMode(subdirectory1)

            subdirectory1 += "/"
            currentTextDirectory = args.txtdir + mode + "/"
            # file level
            for filename in os.listdir(args.imgdir
                                       + subdirectory0
                                       + subdirectory1):
                imagePath = (args.imgdir
                             + subdirectory0
                             + subdirectory1
                             + filename
                             )
                # extract corpus file number from image file
                if mode == "monolingual":
                    corpusFileNr = re.findall("^([0-9]+)_", filename)
                elif mode == "parallel":
                    corpusFileNr = re.findall("^([0-9]+_[A-Z]{2})_", filename)
                else:
                    sys.exit("Fatal error at " + imagePath
                             + " Could not resolve corpus file number.")

                textPath = currentTextDirectory + corpusFileNr[0] + ".txt"
                writeJSON(imagePath, textPath, outfilePath)


if __name__ == "__main__":
    main()
