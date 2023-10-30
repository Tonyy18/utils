import json

class Config:
    def __init__(self, config):
        self.data = config
        if(type(self.data) is str):
            self.data = json.loads(config)

    def get(self, key):
        if(key in self.data):
            return Config(self.data[key])
        raise KeyError("Invalid config key (" + str(key) + ")")

    def value(self):
        return self.data

    @staticmethod
    def read(path="resources/config.json"):
        f = open(path)
        content = f.read()
        f.close()
        return Config(content)
    
    def __str__(self):
        return str(self.data)
