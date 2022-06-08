from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
from variables import expected_result


class GoogleSearchLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.CSS_SELECTOR, 'input[title="Поиск"]')

    LOCATOR_CALCULATOR = (By.CLASS_NAME, 'jlkklc')
    LOCATOR_CALC_BUTTON = (By.CSS_SELECTOR, 'div[aria-label="равно"]')
    LOCATOR_CALC_FIELD = (By.ID, 'cwos')
    LOCATOR_CALC_HISTORY = (By.CLASS_NAME, 'vUGUtc')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        search_field.submit()
        return search_field


    def calculator_send_value(self, send_val):
        calculator = self.find_element(GoogleSearchLocators.LOCATOR_CALCULATOR)
        calculator.click()
        calculator.send_keys(send_val)
        calculator_submit = self.find_element(GoogleSearchLocators.LOCATOR_CALC_BUTTON)
        calculator_submit.click()


    def calculator_get_resultField_test(self):
        resultField = self.find_element(GoogleSearchLocators.LOCATOR_CALC_FIELD).text
        assert resultField == expected_result.exp_result_calc, 'Unexpected value'


    def calculator_get_historyField_test(self):
        historyField = self.find_element(GoogleSearchLocators.LOCATOR_CALC_HISTORY).text
        assert historyField == expected_result.exp_history_calc, 'Unexpected history'
