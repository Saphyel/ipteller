from classes.jsonip import JsonIp
from classes.address import Address
from classes.mailer import Mailer

# Get last IP
address = Address('tmp/address.txt')
address.load()

# Fetch actual IP
provider = JsonIp()

# Report if is new
if provider.ip != address.ip:
    address.ip = provider.ip
    address.save()

    deliver = Mailer()
    deliver.send('something@gmail.com', 'something@gmail.com', 'IP Teller', 'Your IP changed to: ' + address.ip)
