#!/usr/bin/python3


#imports
import sys
import pandas as pd
import argparse
from scipy import stats

#read in data from text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="file name for first data file")
#   parser.add_argument("file2", help="file name for second data file")
    parser.add_argument("col_sep", help = "Which column would you like to seperate the data")
    parser,add_argument("row_sep", help = "Row value to seperate data")
    args =  parser.parse_args()
    #print(args.file1, args.file2 )
    # Import data into dataframes
    df1 = pd.read_csv(args.file1)
#    data2 = pd.read_csv(args.file2)
    data1 = df1[df1.col_sep == row_sep]
    data2 = df1[df1.col_sep != row_sep]

    
