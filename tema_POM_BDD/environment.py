from chrome_browser import Browser

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def before_all(context):
    context.chrome_browser = Browser()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    context.secure_page = SecurePage()
