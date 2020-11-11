#!/bin/bash

#This scripts collect timing for instance deletion using the openstack CLI.
# Number of trials you would like to run, input from args. Default=0
TRIALS=${1:-0}
NAME=${2}
#Set output file name. Uses parameter expansion. 
# If $2 (second command line arg) is not set/null, then set it to whatever is after :-
OUTPUTFILE=${3:-unnamed_data.txt}

# Set command and parameters you would like to test
OS_CMD="openstack server delete" 

#First source the demo credentials
source $CRED

# Delete instances
for (( i=0; i < $TRIALS; i++ ))
do
     INSTANCE_NAME=" $NAME$i"
     { printf "\nTrial #: $i" ; } >>$OUTPUTFILE
     { time $OS_CMD$INSTANCE_NAME; } 2>> $OUTPUTFILE 
    
done

# Run server list command to show that it worked
openstack server list
