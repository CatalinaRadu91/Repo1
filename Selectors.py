import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()



# By ID

chrome.get('https://ro-ro.facebook.com/')
e_mail_phone_field = chrome.find_element(By.ID, 'email')
e_mail_phone_field.send_keys('catalina.radu91@gmail.com')
time.sleep(5)

pass_field = chrome.find_element(By.ID, 'pass').send_keys('Par0l@007')
time.sleep(5)

chrome.get('https://formy-project.herokuapp.com/form')
job_title_field = chrome.find_element(By.ID, 'job-title').send_keys('QA')
time.sleep(5)



# By LINK TEXT - nu trebuie sa deschid mereu inspectorul la link-text; este acelasi ca in pagina

form_link = chrome.find_element(By.LINK_TEXT, 'FORMY').click()
time.sleep(5)

checkbox_link = chrome.find_element(By.LINK_TEXT, 'Checkbox').click()
time.sleep(5)

components_link = chrome.find_element(By.LINK_TEXT, 'Components').click()
time.sleep(5)



# By PARTIAL LINK TEXT

chrome.get('https://the-internet.herokuapp.com/')
selenium_link = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Entry').click()
time.sleep(5)

chrome.get('https://the-internet.herokuapp.com/')
java_script_link = chrome.find_elements(By.PARTIAL_LINK_TEXT, 'Java')[1].click()
time.sleep(5)

chrome.get('https://www.bonprix.ro/')
club_bonprix_link = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Club').click()
time.sleep(5)

livrare_si_plata_link = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Livrare').click()
time.sleep(5)



# By NAME

chrome.get('https://www.saucedemo.com/')
pass_field = chrome.find_element(By.NAME, 'password').send_keys('par0l@nou@')
time.sleep(5)

chrome.get('https://accounts.google.com/v3/signin/identifier?dsh=S-636837424%3A1676799732742494&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHe0bBhj98LQpoh2A74UrK4_e4_WKjrXdB1Z7EDdi8rAxLXqQ1mxeQ8edbWJ2XAB7_Svr_BvGA')
email_field = chrome.find_element(By.NAME,'identifier')
email_field.send_keys('catalina.radu91@gmail.com')
time.sleep(5)

chrome.get('https://contulmeu.reginamaria.ro/')
email_field = chrome.find_element(By.NAME, 'Email').send_keys('xyzasda@yahoo.com')
time.sleep(5)



# By TAG

chrome.get('https://www.saucedemo.com/')
username_field = chrome.find_element(By.TAG_NAME, 'input')
username_field.send_keys('standard_user')
time.sleep(5)

password_field = chrome.find_elements(By.TAG_NAME, 'input')[1]
password_field.send_keys('secret_sauce')
time.sleep(5)

login_button = chrome.find_elements(By.TAG_NAME, 'input')[2]
login_button.click()
time.sleep(5)



# By Class name

# functioneaza doar dupa ce m-am logat pe site (in legatura cu randurile de mai sus)
choose_product = chrome.find_elements(By.CLASS_NAME, 'inventory_item_name')[1]
choose_product.click()
time.sleep(5)

chrome.get('https://formy-project.herokuapp.com//form')
form = chrome.find_elements(By.CLASS_NAME, 'form-control')
form[0].send_keys('Catalina')
form[1].send_keys('Radu')
form[2].send_keys('QA')
form[3].send_keys('0')
form[4].send_keys('02/19/2023')
time.sleep(5)


# ----------------------------------------------------------------------------------------------------------------------

# By CSS

# By ID (#)
chrome.get('https://ro-ro.facebook.com/')
e_mail_phone_field = chrome.find_element(By.CSS_SELECTOR, '#email')
e_mail_phone_field.send_keys('catalina.radu91@gmail.com')
time.sleep(5)


# By Class (.)
chrome.get('https://formy-project.herokuapp.com/form')
first_name_field = chrome.find_element(By.CSS_SELECTOR, '.form-control')
first_name_field.send_keys('Catalina')
time.sleep(5)

last_name_field = chrome.find_elements(By.CSS_SELECTOR, '.form-control')[1]
last_name_field.send_keys('Radu')
time.sleep(5)


# By ATRIBUT = VALOARE ("tag[numele_atributului='valoarea_atributului']")
chrome.get('https://www.saucedemo.com/')
username_field = chrome.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
username_field.send_keys('Ariana')
time.sleep(5)

password_field = chrome.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password_field.send_keys('secret_sauce')
time.sleep(5)

login_button = chrome.find_element(By.CSS_SELECTOR, "input[data-test='login-button']")
login_button.click()
time.sleep(5)


# By ATRIBUT = VALOARE_PARTIALA ("tag[numele_atributului*='valoare_partiala_atribut']")

chrome.get('https://formy-project.herokuapp.com//form')
first_name_field = chrome.find_elements(By.CSS_SELECTOR, "input[placeholder*='Enter']")[0]
first_name_field.send_keys('Catalina')
time.sleep(5)

last_name_field = chrome.find_elements(By.CSS_SELECTOR, "input[placeholder*='Enter']")[1]
last_name_field.send_keys('Radu')
time.sleep(5)


# ----------------------------------------------------------------------------------------------------------------------

# By XPATH !!! pozitia nu incepe de la 0 ci de la 1 (vezi rand 193 si 198)

# ierarhie - parinte - copil - frate (sibling)

# 3 dupa atribut=valoare ('//tag[@atribut = "valoare_atribut"]')
chrome.get('https://www.reginamaria.ro/mamografia-salveaza-vieti?gclid=Cj0KCQiArsefBhCbARIsAP98hXQUsDJspRibVi-Cw9e1W4LoRgnfLYTk12tsB4_Mv7vkJRclicXzIUYaAlJ6EALw_wcB&gclsrc=aw.ds')
nume_field = chrome.find_element(By.XPATH, '//input[@id = "edit-name"]').send_keys('Catalina')
time.sleep(5)

prenume_field = chrome.find_element(By.XPATH, '//input[@id = "edit-surname"]').send_keys('Radu')
time.sleep(5)

oras_field = chrome.find_element(By.XPATH, '//input[@name = "city"]').send_keys('Brasov')
time.sleep(5)



# 3 dupa textul de pe element ('//tag[text() = "textul_din_element"]')
chrome.get('https://the-internet.herokuapp.com/')
contex_menu = chrome.find_element(By.XPATH, '//a[text()= "Context Menu"]').click()
time.sleep(5)

chrome.get('https://the-internet.herokuapp.com/')
buttons = chrome.find_element(By.XPATH, '//a[text()= "Floating Menu"]').click()
time.sleep(3)

chrome.get('https://formy-project.herokuapp.com/form')
time.sleep(3)
form = chrome.find_element(By.XPATH, '//a[text()= "Formy"]').click()
time.sleep(3)

chrome.get('https://discord.com/')
time.sleep(3)
open_in_browser= chrome.find_element(By.XPATH, '//button[text()= "Open Discord in your browser"]').click()
time.sleep(3)

# Denisa, imi zici te rog de ce aici imi da eroare? Pentru ca am un alt link in interiorul tag-ului?
# chrome.get('https://www.bonprix.ro/')
# club_bonprix = chrome.find_element(By.XPATH, '//a[text()= "Club bonprix"]').click()
# time.sleep(3)



# 3 după parțial text ('//tag[contains(text(),  "textul_partial_din_element")]')
chrome.get('https://the-internet.herokuapp.com/')
file_download = chrome.find_element(By.XPATH, '//a[contains(text(), "File")]').click()
time.sleep(5)

chrome.get('https://the-internet.herokuapp.com/')
js_onload_event_error = chrome.find_elements(By.XPATH, '//a[contains(text(), "Java")]')[1]
js_onload_event_error.click()
time.sleep(5)
#SAME WITH:
chrome.get('https://the-internet.herokuapp.com/')
js_onload_event_er = chrome.find_element(By.XPATH, '(//a[contains(text(), "Java")])[2]')
js_onload_event_er.click()
time.sleep(5)

chrome.get('https://the-internet.herokuapp.com/')
infinte_scroll = chrome.find_element(By.XPATH, '//a[contains(text(), "Infinite")]').text
print(infinte_scroll)



# 2 cu SAU, folosind pipe | ('//tag[@atribut = "valoare_atribut"]')

chrome.get('https://formy-project.herokuapp.com/form')
first_name = chrome.find_element(By.XPATH, '//input[@id="last-name"] | //input[@placeholder="Enter last name"]')
first_name.send_keys("Radu")
time.sleep(5)


job_title = chrome.find_element(By.XPATH, '//input[@id="job-title1"] | //input[@id="job-title2"] | //input[@id="job-title"]')
job_title.send_keys("QA")
time.sleep(5)



# 2 cu * (toate elementele care respecta regula)

#indiferent de tag
chrome.get('https://formy-project.herokuapp.com/form')
date_picker = chrome.find_element(By.XPATH, '//*[@id="datepicker"]')
date_picker.send_keys("02/19/2023")
time.sleep(5)
date_picker.clear()

#indiferent de atribut
date_picker = chrome.find_element(By.XPATH, '//input[@*="datepicker"]')
date_picker.send_keys("03/19/2023")
time.sleep(5)



# 2 in care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]

chrome.get('https://formy-project.herokuapp.com/form')
field = chrome.find_elements(By.XPATH, '//input[@*="form-control"]')
field[1].send_keys('xyz')
time.sleep(5)

chrome.get('https://www.saucedemo.com/')
pass_field = chrome.find_elements(By.XPATH, '//input[@class="input_error form_input"]')
pass_field[1].send_keys('yzaca')
time.sleep(5)



# 2 in care sa folosesti parent::
chrome.get('https://formy-project.herokuapp.com/form')
college_button = chrome.find_element(By.XPATH, '//input[@id="radio-button-2"]/parent::div').text
print(college_button)
time.sleep(5)

chrome.get('https://formy-project.herokuapp.com/form')
job_title = chrome.find_elements(By.XPATH, '//*[@type="text"]//parent::div')
print(job_title[2].text)
time.sleep(5)



# 1 IN CARE SA FOLOSESTI FRATELE ANTERIOR SI 1 IN CARE SA ALEGI FRATELE DE DUPA

chrome.get('https://the-internet.herokuapp.com/')
ab_testing = chrome.find_element(By.XPATH, '//a[text()= "Add/Remove Elements"]/parent::li/preceding-sibling::li/a').click()
time.sleep(5)


chrome.get('https://formy-project.herokuapp.com/form')
components = chrome.find_element(By.XPATH, '//a[@id="navbarDropdownMenuLink"]')
components.click()
time.sleep(5)

drag_and_drop = chrome.find_element(By.XPATH, '//a[@href="/datepicker"]/following-sibling::a')
drag_and_drop.click()
time.sleep(5)



# 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez

chrome.get('https://www.elefant.ro/new-account?TargetPipeline=ViewProfileSettings-ViewProfile')
def formy_input(field_name, input_value):
    input = chrome.find_element(By.XPATH, f'//input[@placeholder="{field_name}"]')
    input.clear()
    input.send_keys(input_value)

formy_input('Prenume', 'Catalina')
time.sleep(5)
formy_input('Nume', 'Radu')
time.sleep(5)
formy_input('Adresa de email', 'catalina.radu91@gmail.com')
time.sleep(5)