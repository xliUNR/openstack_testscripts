#!/usr/bin/python2
import os
from keystoneauth1 import loading
from keystoneauth1 import session
import novaclient
from novaclient import client
import keystoneclient.v2_0.client as ksclient

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

def get_nova_cred():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api-key'] = os.environ['OS_PASSWORD']
print "Hello"

creds = get_keystone_cred()
#keystone = ksclient.Client(**creds)

# Load credentials
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(**creds)
sess = session.Session(auth=auth)
# nova credentials
nova = client.Client(2, session=sess)
#client.flavors.list()
#print(nova.flavors.list())
# Launching instances
# First get a flavor
fl = nova.flavors.find(
nova.servers.create("py_test_Cir", flavor-
