from Tools.JsonReader import *
from selenium import webdriver


class Initializer:

    def setUpDriver(self):
        json = JsonReader("Config")
        if json.getData("Browser") == "Chrome":
            self.driver = webdriver.Chrome(json.getData("ChromeDriverPath"))
        self.driver.maximize_window()
        self.driver.get(json.getData("URL"))
        return self.driver



