from json import load
from urllib2 import urlopen

class JsonIp:

    def __init__(self):
        url = 'https://jsonip.com/'
        uri = urlopen(url)
        response = load(uri)
        self.ip = response["ip"]
        # self.ip = '1.1.1.1'
