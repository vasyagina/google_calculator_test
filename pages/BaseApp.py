from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variables import variables


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = variables.start_link

    def find_element(self, locator,time=10):
        return WebDriverWait(self.browser,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.browser.get(self.base_url)