#!/usr/bin/env python

import logging
import requests


class JsonIp(object):
    @staticmethod
    def get_response():
        url = 'https://jsonip.com/'
        try:
            return requests.get(url).json()
        except ValueError as err:
            logging.exception(err)

    @staticmethod
    def get_ip(uri):
        return uri["ip"]
