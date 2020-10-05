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
        instance_name = 'py_timeit_default_'+str(i)
        # start timer
        tic_time, tic_clock, tic_timeit = time.time(), time.clock(), timeit.default_timer()
        nova_launch.launch_instance(instance_name)
        toc_time, toc_clock, toc_timeit = time.time(), time.clock(), timeit.default_timer()
        t_time = toc_time - tic_time
        t_clock = toc_clock - tic_clock
        t_timeit = toc_timeit - tic_timeit
        # write to file
        f.write( 'Trial %d time: %0.4f \n' % (i, t_time) )
        f.write( 'Trial %d clock: %0.4f \n' % (i, t_clock) )
        f.write( 'Trial %d timeit: %0.4f \n' % (i, t_timeit) )

