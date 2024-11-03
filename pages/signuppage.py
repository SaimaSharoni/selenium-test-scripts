from selenium.webdriver.common.by import By
class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.username_field = self.driver.find_element(By.XPATH, "//input[@id='id_username']")
        self.email_field = self.driver.find_element(By.XPATH, "//input[@id='id_email']")
        self.password_field = self.driver.find_element(By.XPATH, "//input[@id='id_password1']")
        self.confirm_password_field = self.driver.find_element(By.XPATH, "//input[@id='id_password2']")
        self.captcha = self.driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border")
        self.submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        
    def signup(self, username, email, password):
        self.username_field.send_keys(username)
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        self.confirm_password_field.send_keys(password)
        self.captcha.is_selected()
        self.submit_button.click()