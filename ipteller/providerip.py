#!/usr/bin/env python

import logging
import requests


class ProviderIp(object):
    def __init__(self):
        self.url = ''

    def get_response(self):
        try:
            return requests.get(self.url).json()
        except ValueError as err:
            logging.exception(err)
