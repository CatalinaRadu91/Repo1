from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, '//button[@class="radius"]')
    ERROR_MSG = (By.ID, "flash")

    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.send_keys(*self.USERNAME, username)
        self.send_keys(*self.PASSWORD, password)
        self.click_element(*self.LOGIN_BTN)

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text

    def login_btn_is_displayed(self):
        self.verify_element_is_displayed(*self.LOGIN_BTN)
