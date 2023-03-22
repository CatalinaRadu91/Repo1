import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

# exemplu de key presses (actiuni diferite de la tastatura/mouse: Backspace, Delete, CTRL, etc)
# pentru asta trebuie sa importam clasa keys

class KeyPresses (unittest.TestCase):

    def setUp(self):
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

    # def tearDown(self):
    #     driver.quit()

    def test_keys(self):
        username = driver.find_element(By.ID, "username")
        username.send_keys("Catalina")
        sleep(2)
        username.clear() #se sterge tot continutul textboxului
        sleep(2)
        username.send_keys(Keys.COMMAND, "Radu")
        sleep(2)
        username.send_keys(Keys.BACK_SPACE *2)
        username.send_keys(Keys.TAB)
        sleep(2)