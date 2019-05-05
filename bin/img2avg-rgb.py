#!/usr/bin/env python
"""
Script to convert an image file to RGB and HSL values
"""
import os
import csv
import argparse
import colorsys
from img import get_img_avg_rgb

def main(**kwargs):
    """
    Main control function for the program
    """
    input = kwargs.pop('input')[0] # list of input items
    input_path = os.path.realpath(input)
    output_file = kwargs.pop('output_file') # file to write sorted list to
    red, green, blue = get_img_avg_rgb(input_path)
    hue, saturation, value = colorsys.rgb_to_hsv(red, green, blue)
    with open(output_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow([ input_path, red, green, blue, hue, saturation, value ])

def parse():
    """
    Parses script args
    """
    parser = argparse.ArgumentParser(
        description='Convert image to average RGB HSV values')
    parser.add_argument('input',
                        nargs=1,
                        help='Image file input')
    parser.add_argument("-o",
        default = "image.rgb.hsv.csv",
        dest = 'output_file',
        help = "Output file to write values to")
    parser.add_argument("--ignore",
        default = None,
        dest = 'ignore_file',
        help = "File containing a comma separated list of RGB values to ignore when calculating the average RBG and HSV values for an image")

    args = parser.parse_args()

    main(**vars(args))

if __name__ == '__main__':
    parse()
