#!/usr/bin/python2
import argparse

def time_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials' ,help='The number of instances you would like to launch', type=int,default=0) 
    parser.add_argument('--output_file', help='The name of the output file to save run time data', default='unnamed_data.txt')
    return parser.parse_args()


    