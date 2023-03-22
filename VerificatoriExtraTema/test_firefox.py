import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

class Firefox(unittest.TestCase):

    def setUp(self):
        driver.get("https://contulmeu.reginamaria.ro/#/Account/Inregistrare")
        driver.maximize_window()

    # def tearDown(self):
    #     driver.quit()

    def test_duplicate_account(self):
        cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        email_address = driver.find_element(By.ID, "email").send_keys("catalina.radu91@gmail.com")
        phone_number = driver.find_element(By.XPATH, "//*[@name='Numar de telefon']").send_keys("0744693615")
        password = driver.find_element(By.ID, "parola").send_keys("Par0l@PA")
        confirm_password = driver.find_element(By.NAME, "Confirmare Parola")
        confirm_password.send_keys("Par0l@PA")
        confirm_password.send_keys(Keys.TAB)
        sleep(3)
        create_account_button = driver.find_element(By.ID, "button-register").click()
        sleep(3)

        actual = driver.find_element(By.XPATH, "//span[@class='k-window-title k-dialog-title']").text

        self.assertEqual("Atentie!", actual, "Logarea s-a realizat chiar daca pe e-mail-ul introdus exista deja un cont")

