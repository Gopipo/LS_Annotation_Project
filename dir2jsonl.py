#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import json

#@CHECKPATH
imageDirectory = "./Corpora/images_webcorpus/"
textDirectory = "./Corpora/tokenized_txt_files/tokenized_"
mode = ""

def getMode(path) -> str:
    """ Pre: file structure is thus that directory containing parallel or
    monolingual text files is marked as such. "_parallel" or "_monolingual"
    must be the end of the directory name.

    Checks whether loop currently is in a parallel or monolingual directory
    and sets mode to the corresponding option..
    """
    currentMode = re.findall("_([A-Za-z0-9]+)$", path)
    return currentMode[0]

def writeJSON(imagePath, textPath):
    """ Appends JSON Lines file with image path and text to be fed to prodigy
    as stream for annotation.
    """
    #read txt file content
    content=""
    with open(textPath, "r", encoding="utf-8") as tf:
        for line in tf:
            content = content + line

    #create JSON format
    dict = {"image": imagePath, "text": content}
    #append file
    #@CHECKPATH
    with open("./Corpora/JSON/imageTextPaired.jsonl", "a", encoding="utf-8") as f:
        json.dump(dict, f)
        f.write("\n")

def check_fileExists():
    """Alert user if .jsonl file already exists."""
    #@CHECKPATH
    if os.path.isfile("./Corpora/JSON/imageTextPaired.jsonl"):
        appendVerification = ""
        while appendVerification != "y" and appendVerification != "n":
            appendVerification = input("The file ./Corpora/JSON/imageTextPaired.jsonl already exists. \n Are you sure you want to append said file with the data in: ./Corpora/images_webcorpus/ \n (y/n): ")
        if appendVerification == "n":
            sys.exit("Execution stopped.")

def main():
    """Pre: Only execute this once. Appends imageTextPaired.jsonl file!
    Exception: completely new set of image data in the given directories.

    Crawls through all image directories, pairs up the image path with the
    corresponding text, appends the pair to the specified .jsonl
    file..
    """
    check_fileExists()

    #@CHECK_STRUCTURE
    # images_html/, images_pdf/
    for subdirectory0 in os.listdir(imageDirectory):
        subdirectory0 += "/"
        # */*_monolingual/, */*_parallel/
        for subdirectory1 in os.listdir(imageDirectory
                                       + subdirectory0):
            mode = getMode(subdirectory1)

            subdirectory1 += "/"
            currentTextDirectory = textDirectory + mode + "/"
            # file level
            for filename in os.listdir(imageDirectory
                                       + subdirectory0
                                       + subdirectory1):
                imagePath = imageDirectory + subdirectory0 + subdirectory1 + filename
                #extract corpus file number from image file
                if mode == "monolingual":
                    corpusFileNr = re.findall("^([0-9]+)_", filename)
                elif mode == "parallel":
                    corpusFileNr =re.findall("^([0-9]+_[A-Z]{2})_", filename)
                else:
                    sys.exit("Fatal error at " + imagePath + " Could not resolve corpus file number.")

                textPath = currentTextDirectory + corpusFileNr[0] + ".txt"
                writeJSON(imagePath, textPath)

if __name__ == "__main__":
    main()
