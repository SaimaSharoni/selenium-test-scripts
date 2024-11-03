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
        self.sign_up_page.enter_username(username)
        self.sign_up_page.enter_email(email)
        self.sign_up_page.enter_password(password)
        self.sign_up_page.enter_confirm_password(password)
        self.sign_up_page.enter_captcha(random.randint(1000, 9999))
        self.sign_up_page.click_submit_button()

        # Assert that the sign up was successful
        self.assertTrue(self.sign_up_page.is_success_message_displayed())

    def test_sign_up_with_empty_username(self):
        # Generate random credentials
        email = random.choice(["user1@example.com", "user2@example.com", "user3@example.com"])
        password = random.choice(["password1", "password2", "password3"])

        # Enter the credentials and submit the form
        self.sign_up_page.enter_username("")
        self.sign_up_page.enter_email(email)
        self.sign_up_page.enter_password(password)
        self.sign_up_page.enter_confirm_password(password)
        self.sign_up_page.enter_captcha(random.randint(1000, 9999))
        self.sign_up_page.click_submit_button()

        # Assert that an error message is displayed for the empty username
        self.assertTrue(self.sign_up_page.is_error_message_displayed("Username cannot be empty"))

    def test_sign_up_with_invalid_email(self):
        # Generate random credentials
        username = random.choice(["user1", "user2", "user3"])
        password = random.choice(["password1", "password2", "password3"])

        # Enter the credentials and submit the form
        self.sign_up_page.enter_username(username)
        self.sign_up_page.enter_email("invalid_email")
        self.sign_up_page.enter_password(password)
        self.sign_up_page.enter_confirm_password(password)
        self.sign_up_page.enter_captcha(random.randint(1000, 9999))
        self.sign_up_page.click_submit_button()

        # Assert that an error message is displayed for the invalid email
        self.assertTrue(self.sign_up_page.is_error_message_displayed("Invalid email address"))

    def test_sign_up_with_mismatched_passwords(self):
        # Generate random credentials
        username = random.choice(["user1", "user2", "user3"])
        email = random.choice(["user1@example.com", "user2@example.com", "user3@example.com"])

        # Enter the credentials and submit the form
        self.sign_up_page.enter_username(username)
        self.sign_up_page.enter_email(email)
        self.sign_up_page.enter_password("password1")
        self.sign_up_page.enter_confirm_password("password2")
        self.sign_up_page.enter_captcha(random.randint(1000, 9999))
        self.sign_up_page.click_submit_button()

        # Assert that an error message is displayed for the mismatched passwords
        #self.assertTrue(self.sign_up_page.)
