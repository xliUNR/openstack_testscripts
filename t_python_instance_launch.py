#!/usr/bin/python2

import nova_launch
import time
import timeit
if __name__ == "__main__":
    # Add argument parser stuff

    # start timer
    tic = timeit.default_timer()
    nova_launch.launch_instance()
    toc = timeit.default_timer()
    # write to file
