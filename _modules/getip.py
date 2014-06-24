# -*- coding: utf-8 -*-
'''
Module for running arbitrary tests
'''

# Import Python libs
import os
import sys
import time
import random
import pprint
import logging
import re
# Import Salt libs
import salt
import salt.version
import salt.loader
import salt.client
import salt.modules
__proxyenabled__ = ['*']

script_stop = ''
system = ''
log = logging.getLogger(__name__)

def test():
  __opts__ = salt.config.minion_config('/etc/salt/minion')
  __salt__ = salt.loader.minion_mods(__opts__)
  return __salt__['test3.test1']()

def  front(service):
  __opts__ = salt.config.minion_config('/etc/salt/minion')
  try:
    services = __pillar__['trs_project']['service']['dealing']
    if service in services:
      ip_list = __grains__['ipv4']
      for ip in ip_list:
        ip_front = re.match(r'10.1.10.*',ip)
        if ip in  ip_front.group():  
          return ip
    else:
      return "FALSE"
  except: #"no dealing service"
    return "FALSE"

