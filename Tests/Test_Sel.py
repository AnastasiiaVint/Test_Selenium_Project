import pytest
from PageObject.TestPage import SearchHelper
from allure_commons.types import AttachmentType
import time

import allure


@pytest.mark.usefixtures("browser")
class Test_google_search_page():

    @allure.feature('Test search')
    @allure.story('Test search')
    def test_search(self, browser):
        try:
            main_page = SearchHelper(browser)
            main_page.go_to_site()
            main_page.enter_words("Hello World")
            time.sleep(3)
            main_page.click_on_the_search_button()
            results = main_page.check_search_result()
            assert "test" in results[0]


        except:

            allure.attach(browser.get_screenshot_as_png(),
                          name="test_screenshot",
                          attachment_type=AttachmentType.PNG)
