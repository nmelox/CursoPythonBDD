from selenium.webdriver.common.by import By


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
        self.commit_button = (By.NAME,"commit")

    
