import json
from selenium import webdriver


class Initializer:

    def __init__(self):
        self.path = "config.json"
        with open(self.path, "r") as config:
            self.file = json.load(config)

    def getData(self, data):
       return self.file[data]

    def setUpDriver(self):
        if self.getData("Browser") == "Chrome":
            self.driver = webdriver.Chrome(self.getData("ChromeDriverPath"))
        self.driver.maximize_window()
        self.driver.get(self.getData("URL"))
        return self.driver