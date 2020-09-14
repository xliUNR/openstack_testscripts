#!/bin/bash

#This scripts collect timing for instance launching using the openstack CLI.

# Variables
CRED="/root/demo-openrc"
IMAGE=""
FLAVOR=""
SECGROUP=""
TRIALS=4
#First source the demo credentials
source $CRED

# Launch an instance
for (( i=0; i < $TRIALS; i++ ))
do
	{ time openstack image list ; } 2>> test.txt 
done
