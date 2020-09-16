#!/bin/bash

#This scripts collect timing for instance launching using the openstack CLI.

# Variables
CRED="/root/demo-openrc"
IMAGE="cirros"
FLAVOR="m.nano"
SECGROUP="default"
KEYPAIR="demotestkey1"
INSTANCE_NAME="time_test $i"
TRIALS=1
# Set output file name. Uses parameter expansion. 
# If $1 (first command line arg) is not set/null, then set it to whatever is after :-
OUTPUTFILE=${1:-unnamed_data.txt}
OS_CMD="openstack server list" 
OS_PARAMS="--flavor $FLAVOR --image $IMAGE --key-name $KEYPAIR --security-group $SECGROUP $INSTANCE_NAME"
#OS_RUN=$OS_CMD $OS_PARAMS
#First source the demo credentials
source $CRED
#$OS_CMD
# Launch an instance
for (( i=0; i < $TRIALS; i++ ))
do
    { printf "\nTrial #: $i" ; } >>$OUTPUTFILE
    #{ time openstack image list ; } 2>> $OUTPUTFILE
    { eval $OS_RUN ; } 2>> $OUTPUTFILE  
done
