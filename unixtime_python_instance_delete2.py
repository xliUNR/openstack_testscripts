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
        instance_name = 'py_launch_' + str(i)
        tic_time = time.time()
        #nova_launch.launch_instance(instance_name
        nova_launch.delete_instance(instance_name)
        rutime = getrusage(RUSAGE_SELF)
        toc_time = time.time()
        t_real = toc_time - tic_time
        t_user = rutime.ru_utime
        t_sys = rutime.ru_stime
        f.write( 'Trial %d real: %0.4f\n' % (i , t_real ) )
        f.write( 'Trial %d user: %0.4f\n' % (i , t_user ) )
        f.write( 'Trial %d sys: %0.4f\n' % (i , t_sys ) )
        f.write( '\n' )

    
