import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import HtmlTestRunner
import sys
sys.path.insert(0,"..")

from pages.signuppage import SignUpPage

class SignUpPage_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://76.150.246.167:186/register/')

    def tearDown(self):
        self.driver.quit()

    def test_sign_up_with_valid_credentials(self):
        # Generate random credentials
        username = random.choice(["user1", "user2", "user3"])
        email = f"{username}@example.com"
        password = random.choice(["password1", "password2", "password3"])

        # Enter the credentials and submit the form
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.signup(username,email,password)

        # Assert that the sign up was successful
        self.assertTrue(self.sign_up_page.is_error_message_displayed("OTP is sent to Your Email."))


if __name__ == '__main__':
    unittest.main()
