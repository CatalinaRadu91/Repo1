import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException

chrome = webdriver.Chrome()

class LoginTC (unittest.TestCase):

    def login(self, username, password):
        self.username = username
        self.password = password

        chrome.find_element(By.NAME, "username").send_keys(username)
        chrome.find_element(By.NAME, "password").send_keys(password)
        chrome.find_element(By.CLASS_NAME, "radius").click()

    # se ruleaza inainte de fiecare test
    def setUp(self):
        # s= Service(ChromeDriverManager().install())
        # self.chrome = webdriver.Chrome(service=s)
        chrome.get("https://the-internet.herokuapp.com/")
        chrome.find_element(By.XPATH, '//a[@href="/login"]').click()

    # se ruleaza dupa fiecare test
    # def tearDown(self):
    #     chrome.quit()


    # verifica daca noul url este corect
    def test_URL(self):
        actual = chrome.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected, actual, "URL-ul catre care s-a facut redirectionarea este incorect")


    # verifica daca titlul paginii este corect
    def test_page_title(self):
        actual = chrome.title
        expected = "The Internet"
        self.assertEqual(expected, actual, "Titlul paginii accesate este incorect")


    # verifica daca textul de pe elementul xpath=//h2 este corect
    def test_Xpath_element(self):
        actual = chrome.find_element(By.XPATH, '//h2').text
        expected = 'Login Page'
        self.assertEqual(expected, actual, "Elementul xpath = //h2 este incorect")


    # verifica daca butonul de login este afisat
    def test_login_button_is_displayed(self):
        button = chrome.find_element(By.TAG_NAME, 'i')
        self.assertTrue(button.is_displayed(), 'Butonul de login nu este afisat')


    # verifica daca atributul href al linkului ‘Elemental Selenium’ este corect
    def test_atribut_href_elemental_is_correct(self):
        actual = chrome.find_element(By.XPATH, "//a[@href='http://elementalselenium.com/']").get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'Atributul href al link-ului "Elemental Selenium" nu este corect.')


    # verifica daca eroarea afisata este corecta atunci cand nu se completeaza campurile username si password
    def test_error_user_pass_fields_empty(self):
        self.login("", "")
        actual = chrome.find_element(By.ID, "flash").text
        expected = "Your username is invalid!\n×"
        self.assertEqual(expected, actual, "Eroarea afisata atunci cand campurile username si password nu sunt completate, nu este cea corecta!")

    # or

    # def test_error_user_pass_fields_empty(self):
    #     chrome.find_element(By.CLASS_NAME, "radius").click()
    #     error = chrome.find_element(By.ID, "flash")
    #     self.assertTrue(error.is_displayed(), "Nu este afisata o eroare atunci cand campurile username si password nu sunt completate.")


    # verifica daca eroarea afisata este corecta atunci cand campurile username si password sunt completate cu date invalide
    def test_error_usser_pass_fields_invalid(self):
        self.login('ala', 'bala')
        actual = chrome.find_element(By.ID, "flash").text
        expected = "Your username is invalid!"
        self.assertTrue(expected in actual, "Eroarea afisata atunci cand datele completate in campurile mandatpry sunt invalide, nu este cea corecta")


    # fara a completa campurile mandatory (user, pass), click pe "x" si verifica daca eroarea a disparut
    # def test_error_disappeared(self):
    #     chrome.find_element(By.XPATH, '//button/i').click()
    #     chrome.maximize_window()
    #     chrome.find_element(By.XPATH, '//a[@href="#"]').click()
    #
    #     try:
    #         chrome.find_element(By.XPATH, '//a[@href="#"]')
    #         raise Exception('Mesajul de eroare este afisat in continuare.')
    #     except NoSuchElementException:
    #         pass


    # ia ca o lista toate //label; verifica ca textul de pe ele să fie cel asteptat (Username si Password)
    def test_label(self):
        label_list = chrome.find_elements(By.XPATH, '//label')
        actual = label_list[0].text
        expected = 'Username'
        self.assertEqual(actual, expected, 'Textul din cadrul "username" label este incorect.')
        actual2 = label_list[1].text
        expected2 = 'Password'
        self.assertEqual(actual2, expected2, 'Textul din cadrul "username" password este incorect.')


    # Completează cu user și pass valide, click login
    # Verifică ca noul url CONTINE /secure
    # Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # Verifică dacă elementul cu clasa=’flash succes’ este displayed
    # Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_link_has_secure_and_flash_succes_dysplayed(self):
        self.login("tomsmith", "SuperSecretPassword!")
        actual = chrome.current_url
        expected = "secure"
        self.assertTrue(expected in actual, 'Link-ul catre care s-a facut redirectionarea in urma logarii nu contine "/secure"')

        try:
            WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="flash success"]')))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 10 secunde dar nu am gasit elementul "flash success".')

        flash_success = chrome.find_element(By.XPATH, '//div[@class="flash success"]')
        self.assertTrue(flash_success.is_displayed(), 'Elementul cu clasa "flash success" nu este afisat')

        actual2 = flash_success.text
        expected2 = "secure area!"
        self.assertTrue(expected2 in actual2, 'Mesajul nu contine textul "secure area".')


    # Completează cu user și pass valide, click login, click logout
    # Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_redirect_url_after_logout(self):
        self.login("tomsmith", "SuperSecretPassword!")
        chrome.find_element(By.XPATH, '//i[@class="icon-2x icon-signout"]').click()
        actual = chrome.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected, actual, "Redirectionarea dupa logout nu s-a realizat catre URL-ul corect.")


    # - Completează user tomsmith
    # - Găsește elementul //h4
    # - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o potențială parolă.
    # - Folosește o structură iterativă prin care să introduci rând pe rând parolele și să apeși pe login.
    # - La final testul trebuie să îmi printeze fie ‘Nu am reușit să găsesc parola' fie ‘Parola secretă este [parola]

    def test_brute_force_password_hacking(self):
        element_h4 = chrome.find_element(By.TAG_NAME, "h4").text
        parola_potentiala = element_h4.split(' ')
        for i in range(len(parola_potentiala)):
            chrome.find_element(By.NAME, "username").send_keys("tomsmith")
            parola = parola_potentiala[i]
            chrome.find_element(By.NAME, "password").send_keys(parola)
            chrome.find_element(By.CLASS_NAME, "radius").click()
            actual = chrome.current_url
            expected = "https://the-internet.herokuapp.com/secure"
            if actual == expected:
                print(f'Parola secreta este {parola}')
                break
            else:
                print('Nu am reusit sa gasesc parola')
