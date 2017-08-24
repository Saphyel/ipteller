#!/usr/bin/env python
"""Address Entity"""

import os.path


class Address(object):
    """Base class for address."""

    def __init__(self, storage):
        if not os.path.exists(storage):
            file(storage, 'w').close()
        self.storage = storage
        self.public_ip = ""

    def load(self):
        """Load from a file the old ip."""
        stored_ip = open(self.storage)
        self.public_ip = stored_ip.readline()
        stored_ip.close()

    def save(self):
        """Save into a file the new ip."""
        stored_ip = open(self.storage, 'w')
        stored_ip.write(self.public_ip)
        stored_ip.close()
