from behave import *


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will run it for us')
def step_impl(context):
    assert context.failed is False


@given('I have a bucket of {color} paint')
def step_impl(context, color):
    pass
