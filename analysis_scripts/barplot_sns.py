#!/usr/bin/python3

#imports
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # parsing stuff
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="Input file path")
    parser.add_argument("plot_title", help="Title for graph")
    # read in data
    args = parser.parse_args()
    # Import data into dataframes
    df1 = pd.read_excel(args.in_file)
    timings = ["real", "user", "sys", "spawn", "build", "cpu"]
    # Calculate statistics
#   data1_q = list(data1.quantile([0,0.25,0.5,0.75]))
#   data2_q = list(data2.quantile([0,0.25,0.5,0.75]))
    
    data_CLI = df1[df1.api == "CLI"]
    data_py = df1[df1.api == "python"]

    # graphing below
    # data for plots
    # x = timing columns: real, user, sys, etc
    # y = time
    # hue = "image"
    # Make a figure for CLI and another for python
    #fig_CLI, ax_CLI = plt.subplots(2,3)
    #fig_py, ax_py = plt.subplots(2,3)
    
    #fig_CLI.suptitle("OpenStack CLI "+args.plot_title, size=15)
    #fig_py.suptitle("Python API "+args.plot_title, size=15)
    # Set custom color palette
    colors = ["#0E2F44","#696969"]
    sns.set_palette(sns.color_palette(colors))
    g = sns.barplot(x="time_type", y="time_val", hue="api", data=df1)
    g.set(xlabel="Timings", ylabel="Time (s)", title=args.plot_title)
#   handles, labels = g1.get_legend_handles_labels()
#   fig_CLI.legend(handles, labels, loc="right", title="Image Type")
#   fig_py.legend(handles, labels, loc="right", title="Image Type")

    plt.show()

