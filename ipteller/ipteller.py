#!/usr/bin/env python
"""This script runs the whole app"""

from os import environ
from address import Address
from ipify import IpIfy
from jsonip import JsonIp
from mailer import Mailer

address = Address('address.txt')
try:
    user = environ["GMAIL_USER"]
    pwd = environ["GMAIL_PASS"]
except KeyError as err:
    print('You need to add the environment variable: %s' % err)
    quit(1)
try:
    provider = environ["IP_PROVIDER"]
    if provider == 'ipify':
        provider = IpIfy()
    else:
        raise KeyError
except KeyError:
    provider = JsonIp()

ip = provider.get_ip(provider.get_response())

if ip != address.load():
    address.save(ip)
    data = {'user': user, 'pwd': pwd, 'subject': 'IP Teller', 'body': 'Your IP changed to: %s' % ip}
    deliver = Mailer().send(data)
