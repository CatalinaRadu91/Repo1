import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

class Chrome(unittest.TestCase):

    def setUp(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()

    # def tearDown(self):
    #     driver.quit()

    def test_right_url(self):
        driver.find_element(By.XPATH,'//a[contains(text(),"Add")]').click()
        actual = driver.current_url
        expected= "https://the-internet.herokuapp.com/add_remove_elements/"

        self.assertEqual(expected, actual, "URL-ul catre care s-a facut redirectionarea nu este cel corect")

    def test_add_element_button(self):
        driver.find_element(By.XPATH, '//a[contains(text(),"Add")]').click()
        driver.find_element(By.XPATH, '//button').click()
        delete_button = driver.find_element(By.CLASS_NAME,'added-manually')

        self.assertTrue(delete_button.is_displayed(), 'Butonul "Delete" nu este afisat -> butonul "Add Element" nu a fost apelat corespunzator')


    def test_delete_button(self):
        driver.find_element(By.XPATH, '//a[contains(text(),"Add")]').click()
        driver.find_element(By.XPATH, '//button').click()
        driver.find_element(By.CLASS_NAME, 'added-manually').click()

        try:
            driver.find_element(By.CLASS_NAME,'added-manually')
        except:
            print('Butonul Delete nu mai este afisat! :)')
