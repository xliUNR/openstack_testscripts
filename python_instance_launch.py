#!/usr/bin/python2
import os
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client


def get_keystone_cred():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_cred():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api-key'] = os.environ['OS_PASSWORD']
print "Hello"


