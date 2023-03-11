#!/usr/bin/env python3

import pandas as pd
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--input", help="input XLSX file", required=True)
parser.add_argument("--output", help="output CSV file", required=True)
args=parser.parse_args()

read_file = pd.read_excel(args.input)
read_file.to_csv(args.output, index = None, header=True) 
