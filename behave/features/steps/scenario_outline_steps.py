from behave import *

@given('a user {username} with password {password}')
def step_impl(context, username, password):
    pass


@when('they submit their credentials')
def step_impl(context):
    pass

@then('login is {result}')
def step_impl(context, result):
    pass
