from PageObject.LoginPage import *
from PageObject.RegisterPage import *
from Tools.Helper import *
import unittest

from PageObject.HomePage import *


class testCases(unittest.TestCase):

    def setUp(self):
        self.configuration = Initializer()
        self.driver = self.configuration.setUpDriver()
        self.HomePage = HomePage(self.driver)
        self.LoginPage = LoginPage(self.driver)
        self.RegisterPage = RegisterPage(self.driver)

    def test_Login(self):
        self.HomePage.click_login()
        self.LoginPage.login_user()


    def test_RegisterUser(self):
        self.HomePage.click_Register()
        self.RegisterPage.create_newUser()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()