import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    # Setup: Initialize Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    yield driver  # Provide the fixture value to the test
    
    # Teardown: Safely close the browser
    driver.quit()