#!/usr/bin/env python
"""This script runs the whole app"""

from address import Address
from jsonip import JsonIp
from mailer import Mailer

address = Address('address.txt')
address.load()

provider = JsonIp()
provider.get_response()

if provider.public_ip != address.public_ip:
    address.public_ip = provider.public_ip
    address.save()

    deliver = Mailer('IP Teller', 'Your IP changed to: ' + address.public_ip)
    deliver.send()
