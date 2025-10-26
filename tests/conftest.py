import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    # Close the browser after the test completes
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    # Perform login using the utility function
    login(driver)
    return driver