#!/usr/bin/python3

#imports
import pandas as pd
import argparse
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # parsing stuff
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="Input file path")
    parser.add_argument("col_sep", help="Column index to seperate data")
    parser.add_argument("row_sep", help="Row value to seperate data, typicallly windows or cirros")
    parser.add_argument("t_col", type=int, help="Integer specifying which column to graph")
    parser.add_argument("plot_title", help="title of plot")
    args = parser.parse_args()
    col_sep = args.col_sep
    # read in data
    args = parser.parse_args()
    col_sep = args.col_sep
    row_sep = args.row_sep
    t_col = args.t_col
    #print(args.file1, args.file2 )
    # Import data into dataframes
    df1 = pd.read_excel(args.in_file)
#    data2 = pd.read_csv(args.file2)
    data1 = df1[df1[args.col_sep] == args.row_sep]
    data2 = df1[df1[args.col_sep] != args.row_sep]
    data1 = data1.iloc[:,args.t_col]
    data2 = data2.iloc[:,args.t_col]
    # Calculate statistics
    data1_q = list(data1.quantile([0,0.25,0.5,0.75]))
    data2_q = list(data2.quantile([0,0.25,0.5,0.75]))
    
    data1_median = data1.median()
    data2_median = data2.median() 
    # graphing below
    merged_data = [data1, data2]
    fig1, ax1 = plt.subplots()
    ax1.set_title(args.plot_title)
    plt.ylabel('Time (s)')
#   plt.xlabel(['Cirros','Windows'])
    ax1.boxplot(merged_data, labels=['CirrOS','Windows'])
    plt.show()

