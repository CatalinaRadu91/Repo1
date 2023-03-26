'''
How to handle Cookies in Selenium WebDriver:
driver.manage().deleteCookie(arg0); // Deletes the specific cookie
driver.manage().deleteCookieNamed(arg0); // Deletes the specific cookie according to the Name
driver.manage().deleteAllCookies(); // Deletes all the cookies
'''

from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()

    # nu am inteles unde folosesc asta....

    # URL = ""
    #
    # @classmethod
    # def get_url(cls):
    #     return cls.URL
