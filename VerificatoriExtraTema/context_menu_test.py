import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class ContextMenu(unittest.TestCase):

    def setUp(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()

    # def tearDown(self):
    #     driver.quit()

    def test_context_menu(self):
        driver.find_element(By.XPATH, '//a[text()="Context Menu"]').click()
        context_menu = driver.find_element(By.ID, "hot-spot")

        # action chains ma ajuta sa pot da click dreapta
        action = ActionChains(driver)
        context_menu = driver.find_element(By.ID, "hot-spot")
        # metoda perform este echivalentul lui click dreapta
        # metoda context_click ma ajuta sa definesc un context in care pot sa fac click dreapa
        # fara metoda context_click nu pot accesa metoda perform() care este adevaratul click dreapta
        action.context_click(context_menu).perform()

        driver.switch_to.alert.accept()
