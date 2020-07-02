import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseurl="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"
    driver=webdriver.Chrome(executable_path="..//drivers//chromedriver.exe")

    @classmethod
    def setUpClass(cls) :
        cls.driver.get(cls.baseurl)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"webpage titles aren't equal")

    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(r"..\\reports"))