#!/usr/bin/env python
"""This Entity gets values from jsonip"""

from json import load
from urllib2 import urlopen


class JsonIp(object):
    """Base class for jsonip."""

    def __init__(self):
        self.url = 'https://jsonip.com/'
        self.public_ip = '1.1.1.1'

    def get_response(self):
        """Returns public IP address"""
        uri = urlopen(self.url)
        response = load(uri)
        self.public_ip = response["ip"]

    def get_ip(self):
        """Returns public IP address"""
        return self.public_ip
