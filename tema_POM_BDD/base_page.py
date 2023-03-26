from chrome_browser import Browser


class BasePage(Browser):
    def send_keys(self, by, selector, text):
        self.driver.find_element(by, selector).send_keys(text)

    def click_element(self, by, selector):
        self.driver.find_element(by, selector).click()

    def get_text_on_element(self, by, selector):
        return self.driver.find_element(by, selector).text

    def verify_element_is_displayed(self, by, selector):
        actual = self.driver.find_element(by, selector)
        assert actual.is_displayed() == True, 'The element is not on page'
