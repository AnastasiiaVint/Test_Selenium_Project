from BaseApp.BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:

    LOCATOR_SEARCH_FIELD = (By.XPATH, "//input[@name='q']")
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "gNO89b")
    LOCSTOR_SEARCH_RESULTS = (By.TAG_NAME, "h3")

class SearchHelper(BasePage):

    def enter_words(self, word):

        self.find_element(Locators.LOCATOR_SEARCH_FIELD).send_keys(word)

    def click_on_the_search_button(self):
        self.find_element(Locators.LOCATOR_SEARCH_BUTTON).click()

    def check_search_result(self):
        search_elements = self.find_elements(Locators.LOCSTOR_SEARCH_RESULTS)
        search_results_headers = [x.text for x in search_elements if len(x.text) > 0]
        return  search_results_headers




