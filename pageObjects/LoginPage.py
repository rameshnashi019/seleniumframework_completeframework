import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configurations.config import TestData
from pageObjects.BasePage import BasePage


class Login(BasePage):
    email = "//input[@id='email']"
    password = "//input[@id='pass']"
    button = "//button[@name='login']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    def get_title(self):
        return self.title()

    def do_login(self, user, passw):
        self.do_sendKeys(self.email, user)
        self.do_sendKeys(self.password, passw)
        self.do_click(self.button)
        time.sleep(5)
