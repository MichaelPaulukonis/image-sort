#!/usr/bin/env python3

# from __future__ import annotations # python 3.7+
import csv
import os
from typing import Generator, Tuple, List, Dict
import shutil
import argparse


def from_csv(csv_file: str) -> List[str]:
    files = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f, delimiter = ',')
        for row in reader:
            files.append(row['path'])
    return(files)

def main(input_csv, output_path):
    filenames = from_csv(input_csv)

    if not os.path.exists(output_path): 
        os.mkdir(output_path)

    for i in range(0, len(filenames)):
        shutil.copyfile(filenames[i], f"{output_path}/{i:03d}.png")

parser = argparse.ArgumentParser(description = 'Process image-sort.csv and create a directory of numerically indexed sorted images')

parser.add_argument('--input_csv', help = 'Input path to dir to target for (re)naming')
parser.add_argument('--output_path', help = 'Output path for renamed files')

args = parser.parse_args()

main(args.input_csv, args.output_path)
