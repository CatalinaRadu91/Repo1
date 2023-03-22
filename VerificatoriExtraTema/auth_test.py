import unittest
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

class Authentication(unittest.TestCase):

    def setUP(self):
        driver.maximize_window()
        driver.implicitly_wait(3)

    # def tearDown(self):
    #     driver.quit()

    def test_auth(self):
        # https://username:password@linkwebsite
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        sleep(3)