import json


class jsonReader:

    def __init__(self):
        self.path = "Config.json"

    def getData(self):
        with open(self.path, "r") as config:
            file = json.load(config)
            item = file
        return item
