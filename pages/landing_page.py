from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LandingPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://opensource-demo.orangehrmlive.com"
        self.username_field = "username"
        self.password_field = "password"
        self.login_button = "[type=submit]"

    def navigate_to_landing_page(self):
        self.driver.get(self.base_url)

    def enter_username(self, username):
        username_field = self.driver.find_element(By.NAME, self.username_field)
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, self.password_field)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, self.login_button)
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_valid_login(self):
        assert "dashboard" in self.driver.current_url, \
            f"Login failed. Current URL: {self.driver.current_url}"
