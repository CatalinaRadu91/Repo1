import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class Alerts(unittest.TestCase):

    def setUp(self):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()

    # def tearDown(self):
    #     driver.quit()

    def test_alert(self):
        alert = driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]')
        alert.click()

        # ne mutam de pe fereastra curenta pe fereastra alerta; am salvat-o in variabila alert_window
        alert_window = driver.switch_to.alert
        # dam click pe  "OK"-ul din cadrul alertei - metoda accept()
        alert_window.accept()
        # validez textul afisat dupa click ok in cadrul alertei
        alert_message = driver.find_element(By.ID,"result").text
        expected_result = "You successfully clicked an alert"

        self.assertEqual(expected_result, alert_message, "Textul afisat nu este corect")

    def test_confirm_ok(self):
        confirm = driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
        confirm.click()
        confirm_window = driver.switch_to.alert
        confirm_window.accept()
        confirm_ok_message = driver.find_element(By.ID,"result").text
        expected_result = "You clicked: Ok"

        self.assertEqual(expected_result, confirm_ok_message, "Textul afisat nu este corect")

    def test_confirm_cancel(self):
        confirm = driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
        confirm.click()
        confirm_window = driver.switch_to.alert
        confirm_window.dismiss()
        confirm_cancel_message = driver.find_element(By.ID,"result").text
        expected_result = "You clicked: Cancel"

        self.assertEqual(expected_result, confirm_cancel_message, "Textul afisat nu este corect")

    def test_prompt(self):
        prompt = driver.find_element(By.XPATH, '//button[text()="Click for JS Prompt"]')
        prompt.click()
        prompt_window = driver.switch_to.alert
        prompt_window.send_keys("You are a JS prompt")
        prompt_window.accept()
        prompt_message = driver.find_element(By.ID,"result").text
        expected_result = "You entered: You are a JS prompt"

        self.assertEqual(expected_result, prompt_message, "Textul afisat nu este corect")

    