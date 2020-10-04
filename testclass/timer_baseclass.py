#!/usr/bin/python2
#Imports
import argparse
import os
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client as nv_client
from glanceclient import client as gc_client
#import keystoneclient.v2_0.client as ks_client
from keystoneclient.v2_0 import client as ks_client
from neutronclient.v2_0 import client as nt_client


class TimerBase:
    # Class attributes
    # Image IDs
    cirros_image_ID = '8ecbbd50-86a0-4948-9a38-e7d978b8e3d3'
    win10_image_ID = '35b5f896-54b7-429f-b3d6-346c10898f58'
    winServer_image_ID = '7d6c8e94-be48-47db-aea4-7eaf27a266a0'
    ubuntu18_image_ID = 'ba010d4f-74ae-447a-8d15-beecc2a55ba1'
    # initialization function
    def __init__(self, flavor, key, sec_group, net_id):
        # Init variables
        self.flavor = 'm1.nano' if flavor is None else flavor
        self.sec_group = ['default'] if sec_group is None else sec_group
        self.net_id = [{'net-id':'638ae64c-53af-41f1-bda6-4ef5430f4b12'}] if net_id is None else net_id
        self.creds = get_keystone_creds()
    # Init credentials
    def get_keystone_cred():
        d = {}
        d['username'] = os.environ['OS_USERNAME']
        d['password'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['project_name'] = os.environ['OS_PROJECT_NAME']
        d['user_domain_name'] = os.environ['OS_USER_DOMAIN_NAME']
        d['project_domain_name'] = os.environ['OS_PROJECT_DOMAIN_NAME']
        return d


    # Init nova
    # init glance
   

    # command line argument parser
    def timer_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('--trials' ,help='The number of instances you would like to launch', type=int,default=0) 
        parser.add_argument('--output_file', help='The name of the output file to save run time data', default='unnamed_data.txt')
        return parser.parse_args()





