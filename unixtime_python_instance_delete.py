#!/usr/bin/python2

import nova_launch
import parser
import sys
from resource import getrusage, RUSAGE_SELF
import time

if __name__ == "__main__":
    # Add argument parser stuff
    args = parser.time_parser()
    # Open file for writing
    f = open(args.output_file, "w")
    f.write( 'Unix like timing provided by resource module and time \n' )
    # loop over trials and get time
    for i in range(args.trials):
        #instance_name = 'py_launch_' + str(i)
        tic_time, tic_rutime = time.time(), getrusage(RUSAGE_SELF)
        #nova_launch.launch_instance(instance_name
        toc_time, toc_rutime = time.time(), getrusage(RUSAGE_SELF)
        t_real = toc_time - tic_time
        t_user = toc_rutime.ru_utime - tic_rutime.ru_utime
        t_sys = toc_rutime.ru_stime - tic_rutime.ru_stime
        f.write( 'Trial %d real: %0.4f\n' % (i , t_real ) )
        f.write( 'Trial %d user: %0.4f\n' % (i , t_user ) )
        f.write( 'Trial %d sys: %0.4f\n' % (i , t_sys ) )
        f.write( '\n' )

    
