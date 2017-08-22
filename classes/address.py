import os.path

class Address:

    def __init__(self, storage):
        if not os.path.exists(storage):
            file(storage, 'w').close()
        self.storage = storage

    def load(self):
        f = open(self.storage)
        self.ip = f.readline()
        f.close()

    def save(self):
        f = open(self.storage, 'w')
        f.write(self.ip)
        f.close()
