import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from pages.landing_page import LandingPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox(service=webdriver.FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


def test_login_with_valid_credentials(driver):
    landing_page = LandingPage(driver)
    landing_page.navigate_to_landing_page()
    landing_page.login("Admin", "admin123")
    landing_page.verify_valid_login()
