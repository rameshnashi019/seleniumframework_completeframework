from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def title(self):
        return self.driver.title

    def do_sendKeys(self, by_locator, text):
        self.driver.find_element(By.XPATH, by_locator).clear()
        self.driver.find_element(By.XPATH, by_locator).send_keys(text)

    def do_click(self, by_locator):
        self.driver.find_element(By.XPATH, by_locator).click()

    def Takescreenshot(self):
        self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
