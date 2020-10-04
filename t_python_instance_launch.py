#!/usr/bin/python2

import nova_launch
import parser
import sys
import time
import timeit
if __name__ == "__main__":
    # Add argument parser stuff
    args = parser.time_parser()
    # Open file for writing
    f = open(args.output_file, "w")
    # loop over number of trials
    for i in range(args.trials):
        # Calculate name of instance
        instance_name = 'py_test_'+str(i)
        # start timer
        tic = timeit.default_timer()
        nova_launch.launch_instance(instance_name)
        toc = timeit.default_timer()
        t = toc - tic
        # write to file
        f.write( 'Trial %d: %0.4f \n' % (i, t) )




