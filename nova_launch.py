# This file includes all setup code to get nova to work. To use this, import it and then call nova.create with the parameters described below.

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


# Get keystone credentials
creds = get_keystone_cred()
# Load credentials
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(**creds)
sess = session.Session(auth=auth)


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

nova = nv_client.Client(2, session=sess)
glance = gc_client.Client(2, session=sess)
neutron = nt_client.Client(2, session=sess)
fl_obj = nova.flavors.find(name=flavor_name)
im_obj = glance.images.get(cirros_image_ID)   