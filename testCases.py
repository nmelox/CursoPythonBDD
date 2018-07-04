import sys
from Tools.Helper import *
import unittest
import time
from PageObject.HomePage import *


class testCases(unittest.TestCase):

    def setUp(self):
        self.configuration = Initializer()
        self.driver = self.configuration.setUpDriver()
        self.HomePage = HomePage(self.driver)

    def test_Login(self):
        self.HomePage.click_login()

    def test_RegisterUser(self):
        self.HomePage.click_Register()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
