#!/usr/bin/env python

from json import load
from urllib2 import urlopen
import logging


class JsonIp(object):

    @staticmethod
    def get_response():
        url = 'https://jsonip.com/'
        try:
            uri = urlopen(url)
            response = load(uri)
            return response["ip"]
        except ValueError as err:
            logging.exception(err)
            return '1.1.1.1'
