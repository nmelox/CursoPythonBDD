from selenium.webdriver.common.by import By
from Tools.JsonReader import *
import unittest
import time

class LoginPage:

    def __init__(self, driver):
        self.username_box = (By.ID, "username")
        self.password_box = (By.ID, "password")
        self.login_btn = (By.ID, "login-submit")
        self.forget_link = (By.CLASS_NAME, "lost_password")
        self.jsonReader = JsonReader("data")
        self.assertTitle = (By.CLASS_NAME, "my-account")
        self.driver = driver

    def login_user(self):
        try:
            self.enter_user()
            self.enter_password()
            self.click_Login()
            self.verify_Login()
        finally:
            self.driver.save_screenshot("Screenshots/Login_" + time.strftime("%y-%m-%d_%H-%M-%S") + ".png")

    def enter_user(self):
        user_name = self.jsonReader.getData("user")
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.username_box).send_keys(user_name)

    def enter_password(self):
        password = self.jsonReader.getData("password")
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.password_box).send_keys(password)

    def click_Login(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.login_btn).click()

    def verify_Login(self):
        tc = unittest.TestCase("__init__")
        self.driver.implicitly_wait(5)
        userLink = self.driver.find_element(*self.assertTitle)
        tc.assertEqual(userLink.text, "My account")