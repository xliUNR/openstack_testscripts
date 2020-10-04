#!/usr/bin/python2
import os
import sys
import time
import timeit
import argparse
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client as nv_client
from glanceclient import client as gc_client
#import keystoneclient.v2_0.client as ks_client
from keystoneclient.v2_0 import client as ks_client
from neutronclient.v2_0 import client as nt_client

# Openstack base class for keystone credentials
class OpenstackTestBase:
    # Class atttributes
    def __init__(self):
        self.creds = get_keystone_creds()
        self.loader = loading.get_plugin_loader('password')
        self.auth = self.loader.load_from_options(**self.creds)
        self.sess = session.Session(auth=self.auth)
    def get_keystone_cred():
        d = {}
        d['username'] = os.environ['OS_USERNAME']
        d['password'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['project_name'] = os.environ['OS_PROJECT_NAME']
        d['user_domain_name'] = os.environ['OS_USER_DOMAIN_NAME']
        d['project_domain_name'] = os.environ['OS_PROJECT_DOMAIN_NAME']
        return d

class NovaLaunchClass(OpenstackTestBase):
    # Image IDs as class variables
    # Define image IDs
    cirros_image_ID = '8ecbbd50-86a0-4948-9a38-e7d978b8e3d3'
    win10_image_ID = '35b5f896-54b7-429f-b3d6-346c10898f58'
    winServer_image_ID = '7d6c8e94-be48-47db-aea4-7eaf27a266a0'
    ubuntu18_image_ID = 'ba010d4f-74ae-447a-8d15-beecc2a55ba1'
    
    # Initialize instance variables
    def __init__(self, flavor, key, sec_group, net_id):
        self.flavor = 'm1.nano' if flavor is None else flavor
        self.sec_group = ['default'] if sec_group is None else sec_group
        self.net_id = [{'net-id':'638ae64c-53af-41f1-bda6-4ef5430f4b12'}] if net_id is None else net_id
    self.nova = nv_client.Client(2, session=self.sess)
    self.glance = gc_client.Client(2, session=self.sess)
    self.neutron = nt_client.Client(session=self.sess)

    try:
        self.fl_obj = self.nova.flavors.find(name=self.flavor)
    except:
        print("The flavor could not be found.")
        sys.exit(1)
    try:
        self.im_obj = self.glance.images.get(self.cirros_image_ID)
    except:
        print("The image could not be found.")
        sys.exit(1)
    
 


