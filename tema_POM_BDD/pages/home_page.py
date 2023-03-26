
from selenium.webdriver.common.by import By

from base_page import BasePage


class HomePage(BasePage):
    FORM_AUTHENTICATION = (By.LINK_TEXT, "Form Authentication")
    JS_ALERTS = (By.LINK_TEXT, "JavaScript Alerts")
    KEY_PRESSES = (By.LINK_TEXT, "Key Presses")

    def navigate_to_homepage(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def access_form_auth(self):
        self.click_element(*self.FORM_AUTHENTICATION)

    def access_js_alerts(self):
        self.click_element(*self.JS_ALERTS)

    def access_key_presses(self):
        self.click_element(*self.KEY_PRESSES)
