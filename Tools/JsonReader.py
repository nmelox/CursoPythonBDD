import json


class JsonReader:

    def __init__(self, fileName):
        if fileName == "Config":
            self.path = "JSON/config.json"
        else:
            self.path = "JSON/data.json"
        with open(self.path, "r") as file:
            self.file = json.load(file)

    def getData(self, data):
        return self.file[data]
