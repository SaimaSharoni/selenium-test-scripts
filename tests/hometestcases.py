import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import sys
sys.path.insert(0,"..")
from pages.homepage import HomePage

class Homepage_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://76.150.246.167:186/')
    
    def tearDown(self):
        self.driver.quit()

    def test_click_service_link(self):
        home_page = HomePage(self.driver)
        home_page.click_service_link()
        self.assertEqual(self.driver.current_url, "http://76.150.246.167:186/#services")

    def test_click_contact_link(self):
        home_page = HomePage(self.driver)
        home_page.click_contact_link()
        self.assertEqual(self.driver.current_url, "http://76.150.246.167:186/contact")

    def test_click_about_us_link(self):
        home_page = HomePage(self.driver)
        home_page.click_about_us_link()
        self.assertEqual(self.driver.current_url, "http://76.150.246.167:186/about")

    def test_click_Download_link(self):
        home_page = HomePage(self.driver)
        home_page.click_download_link()
        self.assertEqual(self.driver.current_url, "http://76.150.246.167:186/#downloads")
    
    def test_stroll_to_footer(self):
        home_page = HomePage(self.driver)
        home_page.scroll_down_slowly()
        

if __name__ == '__main__':
    unittest.main()
