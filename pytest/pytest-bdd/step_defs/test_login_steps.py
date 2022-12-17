import pytest
from pytest_bdd import given, when, then, parsers, scenarios

scenarios('../features/login.feature')

@given(
    parsers.cfparse('a user {username} with password {password}'),
    target_fixture="some_other_fixture"
    )
def given_a_user(username, password):
    return 'some_other_value'


@when('they submit their credentials')
def when_submit_credentials(some_other_fixture):
    print(some_other_fixture)


@then(
    parsers.cfparse('login is {result}')
)
def then_login(result):
    pass
