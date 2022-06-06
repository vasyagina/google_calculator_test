from GoPages import SearchHelper
import variables
import expected_result


def test_google_calculator_value(browser):
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word(variables.word)
    result_calc, history_calc = google_main_page.calculator_input_value(variables.send_val)
    assert (expected_result.exp_result_calc, result_calc, "Unexpected result")
    assert (expected_result.exp_history_calc, history_calc, "Unexpected history")
