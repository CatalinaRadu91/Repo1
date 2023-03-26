from behave import *


@given('HomePage: the user is on homepage')
def step_impl(context):
    context.home_page.navigate_to_homepage()


@when('HomePage: user clicks on Form Authentication')
def step_impl(context):
    context.home_page.access_form_auth()


@then('LoginPage: user is redirected to Login Page')
def step_impl(context):
    context.login_page.login_btn_is_displayed()
