import time

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    time.sleep(4)

    yield driver
    driver.quit()
