from PageObject.Helper import *
import unittest
import time


class testCases(unittest.TestCase):

    def setUp(self):
        self.configuration = jsonReader()
        self.driver = self.configuration.setUpDriver()

    def test_checkLogin(self):
        self.driver.find_element_by_class_name("login").click()

    def tearDown(self):
        self.driver.save_screenshot("Screenshots/Screenshot"+ time.strftime("%y-%m-%d_%H-%M") +".png")
        self.driver.close()
        self.driver.quit()