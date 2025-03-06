import pytest
from Configurations.config import TestData
from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import Login
from testCases.test_base import BaseTest
from utilies import XLUtils


class Test_002_DDT_Login(BaseTest):

    def test_login(self):
        self.rows = XLUtils.getrownum(TestData.Path, 'Sheet1')
        for r in range(2, self.rows + 1):
            self.user=XLUtils.readdata(TestData.Path,"Sheet1",r,1)
            self.passw=XLUtils.readdata(TestData.Path,"Sheet1",r,2)
            self.lp=Login(self.driver)
            self.lp.do_login(self.user,self.passw)
            title = self.lp.get_title()
            if title == TestData.TITLE:

                assert True
            else:
                self.ba=BasePage(self.driver)
                self.ba.Takescreenshot()
                assert False
