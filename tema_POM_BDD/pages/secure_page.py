from base_page import BasePage

from selenium.webdriver.common.by import By




class SecurePage(BasePage):
    LOGOUT_BTN = (By.CLASS_NAME, 'icon-signout')
    SUCCESS_MSG = (By.CLASS_NAME,'success')

    def navigate_to_secure_page(self):
        self.driver.get("https://the-internet.herokuapp.com/secure")

    def click_logout_btn(self):
        self.click_element(*self.LOGOUT_BTN)

    def verify_success_msg(self):
        self.verify_element_is_displayed(*self.SUCCESS_MSG)
