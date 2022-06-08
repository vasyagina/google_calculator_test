import pytest
from pages.GoPages import SearchHelper
from variables import variables, expected_result


@pytest.mark.newmarker
def test_google_calculator_value(browser):
    print("\nverification result calculation value")
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word(variables.word)
    google_main_page.calculator_send_value(variables.send_val)
    google_main_page.calculator_get_resultField_test()



@pytest.mark.newmarker
def test_google_calculator_history(browser):
    print("\nverification result calculation history")
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word(variables.word)
    google_main_page.calculator_send_value(variables.send_val)
    google_main_page.calculator_get_historyField_test()

