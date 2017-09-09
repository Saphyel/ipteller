#!/usr/bin/env python
"""This script runs the whole app"""

from address import Address
from jsonip import JsonIp
from mailer import Mailer

address = Address('address.txt')
provider = JsonIp()
ip = provider.get_ip(provider.get_response())

if ip != address.load():
    address.save(ip)
    deliver = Mailer('IP Teller', 'Your IP changed to: ' + ip).send()
