#!/bin/bash

#This scripts collect timing for instance launching using the openstack CLI.

# Declare variables
CRED="/root/demo-openrc"
IMAGE="cirros"
FLAVOR="m1.nano"
SECGROUP="default"
KEYPAIR="demotestkey1"
INSTANCE_NAME="time_test"
NETWORK="selfservice"

# Number of trials you would like to run
TRIALS=2

#Set output file name. Uses parameter expansion. 
# If $1 (first command line arg) is not set/null, then set it to whatever is after :-
OUTPUTFILE=${1:-unnamed_data.txt}

# Set command and parameters you would like to test
OS_CMD="openstack server create" 
OS_PARAMS=" --flavor $FLAVOR --image $IMAGE --key-name $KEYPAIR --network $NETWORK --security-group $SECGROUP"

# Combine command and parameters into one 
OS_RUN=$OS_CMD$OS_PARAMS

#First source the demo credentials
source $CRED

# Launch an instance
for (( i=0; i < $TRIALS; i++ ))
do
     INSTANCE_NAME=" time_test$i"
     { printf "\nTrial #: $i" ; } >>$OUTPUTFILE
     { time $OS_RUN$INSTANCE_NAME; } 2>> $OUTPUTFILE 
    
done
