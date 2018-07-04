from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.login_link = (By.CLASS_NAME, "login")
        self.register_link = (By.CLASS_NAME, "register")
        self.download_link = (By.CLASS_NAME, "download")

    def click_Register(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.register_link).click()

    def click_login(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.login_link).click()
