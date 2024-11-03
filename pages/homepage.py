from selenium.webdriver.common.by import By
import time
class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
       
        
        
        self.service_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Services')]")
        self.contact_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
        self.aboutus_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'About Us')]")
        self.download_link = self.driver.find_element(By.XPATH,"//body/section[@id='title']/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]")
        #self.footer_link = self.driver.find_element(By.ID,"support")



    def is_logo_displayed(self):
        return self.logo.is_displayed()

    def click_service_link(self):
        self.service_link.click()

    def click_contact_link(self):
        self.contact_link.click()

    def click_about_us_link(self):
        self.aboutus_link.click()

    def click_download_link(self):
        self.download_link.click()

    def scroll_down_slowly(self):
        height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, height, 100):
            self.driver.execute_script("window.scrollTo(0, " + str(i) + ")")
            time.sleep(1)
    #def scroll_to_footer(self):
        #scroll_to_footer(self.driver)


    