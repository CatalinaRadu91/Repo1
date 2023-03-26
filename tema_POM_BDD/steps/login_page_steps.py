from behave import *


@given('LoginPage: the user is on login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('LoginPage: user enters valid {username} and valid {password} and presses login button')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@then('SecurePage: user is redirected to secure page')
def step_impl(context):
    context.secure_page.verify_success_msg()


@when('LoginPage: user enters invalid {username} and valid {password} and presses login button')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@then('LoginPage: user sees an error message')
def step_impl(context):
    assert context.login_page.get_error_message() == "Your username is invalid!\n×"


@when('LoginPage: user enters valid {username} and invalid {password} and presses login button')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@then('LoginPage: user sees an error message: " Your password is invalid!"')
def step_impl(context):
    assert context.login_page.get_error_message() == "Your password is invalid!\n×"


@when('LoginPage: user enters invalid username and invalid password and presses login button')
def step_impl(context):
    context.login_page.login("alabala", "portocala")


@then('LoginPage: user sees an error message: "Your username is invalid!"')
def step_impl(context):
    assert context.login_page.get_error_message() == "Your username is invalid!\n×"
