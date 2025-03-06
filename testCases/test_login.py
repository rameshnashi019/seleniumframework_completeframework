import pytest
from Configurations.config import TestData
from pageObjects.LoginPage import Login
from testCases.test_base import BaseTest


class Test_001(BaseTest):
    def test_00(self):
        self.lp = Login(self.driver)
        title = self.lp.get_title()
        print(title)
        assert title == TestData.TITLE

    def test_01(self):
        self.lp = Login(self.driver)
        self.lp.do_login(TestData.USERNAME,TestData.PASSWORD)
        title = self.lp.get_title()
        print(title)
        assert title == TestData.Home_page

