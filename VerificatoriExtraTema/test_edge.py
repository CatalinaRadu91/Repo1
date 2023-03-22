import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Edge()

class Edge(unittest.TestCase):

    def setUp(self):
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

    # def tearDown(self):
    #     driver.quit()

    def test_login(self):
        username = driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        password = driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")
        login_button = driver.find_element(By.CLASS_NAME, "radius").click()

        message_displayed = driver.find_element(By.CLASS_NAME, "subheader").text
        expected_result = "Welcome to the Secure Area. When you are done click logout below."

        self.assertEqual(expected_result, message_displayed, "Mesajul afisat este incorect")



    def test_logut(self):
        username = driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        password = driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")
        login_button = driver.find_element(By.CLASS_NAME, "radius").click()

        logout_button = driver.find_element(By.CLASS_NAME, "secondary").click()
        sleep(2)