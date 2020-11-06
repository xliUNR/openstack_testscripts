#!/usr/bin/python3


#imports
import sys
import pandas as pd
import argparse


#read in data from text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="file name for first data file")
    parser.add_argument("file2", help="file name for second data file")
    args =  parser.parse_args()
    #print(args.file1, args.file2 )
    # Import data into dataframes
    data1 = pd.read_csv(args.file1)
    data2 = pd.read_csv(args.file2)

