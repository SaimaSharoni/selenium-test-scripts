class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_field = self.driver.find_element(By.ID, "username")
        self.password_field = self.driver.find_element(By.ID, "password")
        self.login_button = self.driver.find_element(By.ID, "login-button")

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()