#!/usr/bin/python2

# First import nova_launch
import nova_launch
import timeit
import sys
import argparse




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials' ,help='The number of instances you would like to launch', type=int,default=0) 
    parser.add_argument('--output_file', help='The name of the output file to save run time data', default='unnamed_data.txt')
    args = parser.parse_args()


    # Open a file for printing
    f = open(args.output_file,"a+")
    t = timeit.timeit('nova_launch.nova.servers.create(instance_name, im_obj, fl_obj, security_groups=sec_group, key_name=key_name, nics=network_id)', setup='import nova_launch')
    f.write('Trial %d: %0.4f \n' % (i , t))
