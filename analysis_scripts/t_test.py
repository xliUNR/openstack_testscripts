#!/usr/bin/python3


#imports
import pandas as pd
import argparse


#read in data from text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(file1, help="file name for first data file")
    parser.add_argument(file2, help="file name for second data file")

    print(parser.file1, parser.file2)
