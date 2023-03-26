from behave import *


@given('SecurePage: the user is on secure_page')
def step_impl(context):
    context.secure_page.navigate_to_secure_page()


@when('SecurePage: user clicks on logout button')
def step_impl(context):
    context.secure_page.click_logout_btn()


@then('LoginPage: user is directed to Login Page')
def step_impl(context):
    context.login_page.login_btn_is_displayed
