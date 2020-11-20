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
    parser.add_argument("row_sep", help = "Row value to seperate data")
    parser.add_argument("t_col", type=int,help = "Integer specifying which column to do t testing on")
    args = parser.parse_args()
    col_sep = args.col_sep
    row_sep = args.row_sep
    t_col = args.t_col
    #print(args.file1, args.file2 )
    # Import data into dataframes
    df1 = pd.read_excel(args.file1)
#    data2 = pd.read_csv(args.file2)
    data1 = df1[df1[args.col_sep] == args.row_sep]
    data2 = df1[df1[args.col_sep] != args.row_sep]
#   t_input1 = data1[col_sep]
    t_input1 = data1.iloc[:,args.t_col]
    t_input2 = data2.iloc[:,args.t_col]
    t,p = stats.ttest_ind(t_input1, t_input2)
    print("Data Column Name:",t_input1.name)
    print("T-statistic",t, "\nP-statistic:",p)
    
