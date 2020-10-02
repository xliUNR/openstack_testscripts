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
# Define functions
def get_keystone_cred():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_name'] = os.environ['OS_PROJECT_NAME']
    d['user_domain_name'] = os.environ['OS_USER_DOMAIN_NAME']
    d['project_domain_name'] = os.environ['OS_PROJECT_DOMAIN_NAME']
    #d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

#def get_nova_cred():
#    d = {}
#    d['username'] = os.environ['OS_USERNAME']
#    d['api-key'] = os.environ['OS_PASSWORD']
#print "Hello"

def launch_instance():
    nova.servers.create(instance_name, im_obj, fl_obj, security_groups=sec_group, key_name=key_name, nics=network_id)
    #f.write(

if __name__ == "__main__":
   # Define variables
    flavor_name = 'm1.nano'
    key_name = 'demotestkey1'
    sec_group = ['default'] # Must be a list
    network_id = [{'net-id': '638ae64c-53af-41f1-bda6-4ef5430f4b12' }] # Must be a dict
    # Define image IDs
    cirros_image_ID = '8ecbbd50-86a0-4948-9a38-e7d978b8e3d3'
    win10_image_ID = '35b5f896-54b7-429f-b3d6-346c10898f58'
    winServer_image_ID = '7d6c8e94-be48-47db-aea4-7eaf27a266a0'
    ubuntu18_image_ID = 'ba010d4f-74ae-447a-8d15-beecc2a55ba1'

     
    # Set up argparser
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials' ,help='The number of instances you would like to launch', type=int,default=0) 
    parser.add_argument('--output_file', help='The name of the output file to save run time data', default='unnamed_data.txt')
    args = parser.parse_args()
    # Get keystone credentials
    creds = get_keystone_cred()
    #keystone = ksclient.Client(**creds)

    # Load credentials
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(**creds)
    sess = session.Session(auth=auth)
    
    setup_code="""
nova = nv_client.Client(2, session=sess)
glance = gc_client.Client(2, session=sess)
neutron = nt_client.Client(2, session=sess)
fl_obj = nova.flavors.find(name=flavor_name)
im_obj = glance.images.get(cirros_image_ID)
    """
    SETUP = '''
    # nova client initialization
    #nova = nv_client.Client(2, session=sess)
    # Glance client
    glance = gc_client.Client(2, session=sess)
    # Neutron client initialization
    neutron = nt_client.Client(session=sess)
    #print neutron.list_networks(name='selfservice')

        # Launching instances
        # Set all parameters for instance launching
        # Set flavor
    try:
        fl_obj = nova.flavors.find(name=flavor_name)
    except:
        print("The flavor could not be found.")
        sys.exit(1)
        # Set Image
    try: 
        im_obj = glance.images.get(cirros_image_ID)
    except:
        print("The image could not be found.")
        sys.exit(1)
   
    '''
 	# Open a file for printing
    f = open(args.output_file,"a+")
    # loop for number of trials
    for i in range(args.trials):
        #instance_name = 'py_test_'+str(i)
        #tic = time.time()
                # create a server
        #t = timeit.timeit(nova.servers.list())
        #nova.servers.list()
        t = timeit.timeit('nova.servers.create(instance_name, im_obj, fl_obj, security_groups=sec_group, key_name=key_name, nics=network_id)', setup_code)
        #t = timeit.timeit()
        #toc = time.time()
        #t = toc - tic
        f.write('Trial %d: %0.4f \n' % (i , t))
        #print( toc-tic)
   # Launch the instance using the nova create function with timing
    #tic = time.time()
    #nova.servers.create(instance_name, im_obj, fl_obj, security_groups=sec_group, key_name=key_name, nics=network_id)
    #nova.servers.list()
    #toc = time.time()
    # Print output to file
    #f.write('Trial %')
        
        
    #print "Elapsed Time:",toc-tic 
    #print args.trials
    #print args.output_file
