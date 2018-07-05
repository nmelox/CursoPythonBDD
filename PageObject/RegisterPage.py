from selenium.webdriver.common.by import By
from Tools.JsonReader import *
import unittest
import time

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.id_box = (By.ID, "user_login")
        self.password_box = (By.ID, "user_password")
        self.confirmPass_box = (By.ID,"user_password_confirmation")
        self.name_box = (By.ID,"user_firstname")
        self.lastname_box = (By.ID,"user_lastname")
        self.email_box = (By.ID,"user_mail")
        self.language_select = (By.ID,"user_language")
        self.commit_btn = (By.NAME,"commit")
        self.jsonReader = JsonReader("data")

    def create_newUser(self):
        try:
            self.enter_userName()
            self.enter_password()
            self.enter_confirmPassword()
            self.enter_name()
        finally:
            self.driver.save_screenshot("Screenshots/RegisterUser_" + time.strftime("%y-%m-%d_%H-%M-%S") + ".png")

    def enter_userName(self):
        user_name = self.jsonReader.getData("newUser")
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.id_box).send_keys(user_name)

    def enter_password(self):
        password = self.jsonReader.getData("password")
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.password_box).send_keys(password)

    def enter_confirmPassword(self):
        password = self.jsonReader.getData("password")
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.confirmPass_box).send_keys(password)

    def enter_name(self):
        name = self.jsonReader.getData("name")
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.name_box).send_keys(name)