#!/usr/bin/env python
"""This script runs the whole app"""

from classes.address import Address
from classes.jsonip import JsonIp
from classes.mailer import Mailer

ADDRESS = Address('tmp/address.txt')
ADDRESS.load()

PROVIDER = JsonIp()
PROVIDER.get_response()

if PROVIDER.public_ip != ADDRESS.public_ip:
    ADDRESS.public_ip = PROVIDER.public_ip
    ADDRESS.save()

    DELIVER = Mailer('IP Teller', 'Your IP changed to: ' + ADDRESS.public_ip)
    DELIVER.send()
