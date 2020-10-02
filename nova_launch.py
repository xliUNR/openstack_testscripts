#!/usr/bin/python2

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
