#!/usr/bin/env python

import logging
import os.path


class Address(object):
    def __init__(self, storage):
        if not os.path.exists(storage):
            logging.warning('Creating file: ' + storage)
            file(storage, 'w').close()
        self.storage = storage

    def load(self):
        stored_ip = open(self.storage)
        return stored_ip.readline()

    def save(self, ip):
        stored_ip = open(self.storage, 'w')
        stored_ip.write(ip)
        stored_ip.close()
