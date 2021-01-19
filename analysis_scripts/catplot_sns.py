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
    fig_CLI, ax_CLI = plt.subplots(2,3)
    fig_py, ax_py = plt.subplots(2,3)
    fig_CLI.suptitle("OpenStack CLI "+args.plot_title, size=15)
    fig_py.suptitle("Python API "+args.plot_title, size=15)
    # Set custom color palette
    colors = ["#0E2F44","#696969"]
    sns.set_palette(sns.color_palette(colors))

    for i in range(2):
        for j in range(3):
            g1 = sns.stripplot(x="time_type", y="time_val", hue="image",data=data_CLI[data_CLI.time_type == timings[i*3+j]], ax=ax_CLI[i][j])
            g2 = sns.stripplot(x="time_type", y="time_val", hue="image", data=data_py[data_py.time_type == timings[i*3+j]], ax=ax_py[i][j])
            if j == 0:
                g1.set(xlabel="", ylabel="Time (s)")
                g2.set(xlabel=None, ylabel="Time (s)")
            else:
                g1.set(xlabel="", ylabel="")
                g2.set(xlabel=None, ylabel="")

            #g1.set_xticklabels(g1.get_xlabels(),size=15)
            #_,xlabels = ax_CLI.get_xticklabels()
            g1.set_xticklabels(g1.get_xticklabels(), size=15)
            g2.set_xticklabels(g2.get_xticklabels(), size=15)
            g1.get_legend().remove()
            g2.get_legend().remove()
            #handles, labels = g1.get_legend_handles_labels()
            #l = g1.legend(handles[1:3], labels[1:3])
    handles, labels = g1.get_legend_handles_labels()
    fig_CLI.legend(handles[1:3], labels[1:3],loc="right", title="Image Type")
    fig_py.legend(handles[1:3], labels[1:3],loc="right", title="Image Type")
    plt.show()

