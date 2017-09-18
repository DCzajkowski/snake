import json

class Database:
    db = None
    filename = None

    def __init__(self, filename):
        dbFile = open(filename, 'r')
        self.db = json.loads(dbFile.read())
        dbFile.close()

        self.filename = filename

    def read(self, key = None):
        return self.db if key is None else self.db[key]

    def change(self, key, value):
        self.db[key] = value
        self.save()

    def save(self):
        self.write(json.dumps(self.db))

    def write(self, data):
        dbFile = open(self.filename, 'w')
        dbFile.write(data)
        dbFile.close()
