import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.insert(0,"..")
from pages.loginpage import LoginPage

class loginpage_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://76.150.246.167:186/login/')
    
    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("saima", "8 characters.")
        self.assertTrue(self.driver.current_url == "http://76.150.246.167:186/")

    def test_invalid_username(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_username", "8 characters.")
        self.assertTrue(self.driver.current_url == "http://76.150.246.167:186/login/")

    def test_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login("saima", "invalid_password")
        self.assertTrue(self.driver.current_url == "http://76.150.246.167:186/login/")

    def test_empty_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login("", "")
        self.assertTrue(self.driver.current_url == "http://76.150.246.167:186/login/")



if __name__ == '__main__':
    unittest.main()
