from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

class Test_homework():

    def test_first(self):
        driver = webdriver.Chrome()

        driver.get("https://google.com")
        time.sleep(4)
        driver.quit()


