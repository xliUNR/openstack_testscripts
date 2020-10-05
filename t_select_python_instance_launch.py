#!/usr/bin/python2

import nova_launch
import parser
import sys
import time
import timeit

USE_TIMEIT_DEFAULT = 0
USE_TIME_TIME = 0
USE_TIME_CLOCK = 1

if __name__ == "__main__":
    # Add argument parser stuff
    args = parser.time_parser()
    # Open file for writing
    f = open(args.output_file, "w")
    # loop over number of trials
    if USE_TIMEIT_DEFAULT:
        f.write( 'Timed using timeit.default_timer()\n' )
        for i in range(args.trials):
            # Calculate name of instance
            instance_name = 'py_timeit_default_'+str(i)
            # start timer
            tic = timeit.default_timer()
            nova_launch.launch_instance(instance_name)
            toc = timeit.default_timer()
            t = toc - tic
            # write to file
            f.write( 'Trial %d: %0.4f \n' % (i, t) )
    elif USE_TIME_TIME:
        f.write( 'Timed using time.time()\n')
        for i in range(args.trials):
            # Calculate name of instance
            instance_name = 'py_time_time_'+str(i)
            # start timer
            tic = time.time()
            nova_launch.launch_instance(instance_name)
            toc = time.time()
            t = toc - tic
            # write to file
            f.write( 'Trial %d: %0.4f \n' % (i, t) )
    elif USE_TIME_CLOCK:
        f.write( 'Timed using time.clock()\n')
        for i in range(args.trials):
            # Calculate name of instance
            instance_name = 'py_time_clock_'+str(i)
            # start timer
            tic = time.clock()
            nova_launch.launch_instance(instance_name)
            toc = time.clock()
            t = toc - tic
            # write to file
            f.write( 'Trial %d: %0.4f \n' % (i, t) )
    else:
        print( 'No Timer selected!')








