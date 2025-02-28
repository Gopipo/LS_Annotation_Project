#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageChops
from PIL import UnidentifiedImageError
from argparse import ArgumentParser

import xml.etree.ElementTree as ET
import os
import re



def removeKeepFirst(rmdict):
    """
    Keeps first instance of every group of equal images per text.
    Removes the rest..
    """
    for key in rmdict.keys():
        index = 0
        indexlist = []
        # ensure that there are at least 2 elements left to check
        while len(rmdict[key]) >= index+2:
            current = Image.open(rmdict[key][index])
            marker = index+1
            for element in rmdict[key][index+1:]:
                comparison = Image.open(rmdict[key][marker])
                # check size
                if current.size == comparison.size:
                    try:
                        diff = ImageChops.difference(current, comparison)
                        # empty (False) if equal
                        difference = diff.getbbox()
                        if not difference:
                            # mark for removal as not to change list length during loop
                            indexlist.append(marker)
                    # corrupted images generate os.error -2
                    except:
                        # mark for removal as not to change list length during loop
                        indexlist.append(marker)
                marker += 1
            # remove list elements from rear as not to change indices
            indexlist.sort(reverse=True)
            for ind in indexlist:
                # remove file
                os.remove(rmdict[key][ind])
                # remove list entry
                rmdict[key].pop(ind)
            index += 1

def dictifyRmset(rmset):
    """
    Creates a dictionary where keys are text numbers and values are a list of images marked for removal in those texts.
    """
    rmdict={}
    for element in rmset:
        txtName = re.search(r"(\d+)_", element)[1]
        try:
            rmdict[txtName].append(element)
        except KeyError:
            rmdict[txtName] = [element]


def main(args):
    """
    Checks image sizes and removes those below a given height or width.
    Also removes images with a aspect ratio above 1:7.
    Also removes images that cannot be opened by PIL..
    """
    for dir in args.imgdir:
        rmset = set()
        for image in os.listdir(dir):
            image = os.path.join(dir, image)
            width = 100
            height = 100
            if image[-3:] == "svg":
                tree = ET.parse(image)
                root = tree.getroot()
                attribs = root.attrib
                try:
                    width = attribs["width"]
                    height = attribs["height"]
                except KeyError:
                    #if no default resolution is given, keep it.
                    continue
            else:
                try:
                    with Image.open(image) as im:
                        width, height = im.size
                except UnidentifiedImageError:
                    rmset.add(image)
            # 16px chosen due to this being the smallest size of icons under Windows
            if (int(width) < 16 or int(height) < 16) or (int(width)/int(height) > 7 or int(width)/int(height) < 0.14):
                rmset.add(image)
        if args.keepfirst:
            dictifyRmset(rmset)
        else:
            for element in rmset:
                os.remove(element)


def parse_args():
    parser = ArgumentParser(description="Set the image directories in which to remove tiny pictures and select whether to keep first of equal tiny images per text.")
    parser.add_argument("-i", "--imgdir",
                        help="Set the image directories in which to remove tiny pictures.",
                        nargs = "+")
    parser.add_argument("-k", "--keepfirst",
                        help="Does not delete the first of equal tiny pictures per text.",
                        action="store_true",
                        required = False)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
