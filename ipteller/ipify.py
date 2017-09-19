#!/usr/bin/env python

from providerip import ProviderIp


class IpIfy(ProviderIp):
    def __init__(self):
        ProviderIp.__init__(self)
        self.url = 'https://api.ipify.org?format=json'

    @staticmethod
    def get_ip(uri):
        return uri["ip"]
