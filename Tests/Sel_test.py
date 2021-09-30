from allure_commons.types import AttachmentType
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import allure

class Test_homework():

    @allure.feature('Test edit 222')
    def test_first(self):
        pass
        # driver = webdriver.Chrome()
        #
        # driver.get("https://google.com")
        # allure.attach(driver.get_screenshot_as_png(),
        #               name="test_screenshot",
        #               attachment_type=AttachmentType.PNG)
        # time.sleep(4)
        # driver.quit()
