import uuid

import pytest
from appium import webdriver
from pytest_bdd import given, when, then, parsers, scenarios
from pages.catalog_page import CatalogPage
from pages.product_detail_page import ProductDetailPage

scenarios('../features/add_items_to_cart.feature')

@pytest.fixture
def browser():
    caps = {}
    caps['platformName'] = 'Android'
    caps['appium:app'] = 'storage:filename=Android-MyDemoAppRN.1.3.0.build-244.apk'  # The filename of the mobile app
    caps['appium:deviceName'] = 'Google Pixel 6 Pro GoogleAPI Emulator'
    caps['appium:platformVersion'] = '12.0'
    caps['appium:automationName'] = 'UiAutomator2'
    caps['sauce:options'] = {}
    caps['sauce:options']['appiumVersion'] = '1.22.1'
    caps['sauce:options']['build'] = str(uuid.uuid4())
    caps['sauce:options']['name'] = 'Let us test this configuration'

    url = "https://basdijkstra:22105028-d602-4896-b824-d522da578fa9@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(url, caps)
    yield driver
    driver.quit()

@given('Bob has an empty shopping cart')
def step_impl(browser):
    pass

@when('he adds two backpacks to the cart')
def step_impl(browser):
    CatalogPage(browser).select_first_product()
    ProductDetailPage(browser).add_items_to_cart()

@then(parsers.cfparse(
    'the number of items in his shopping cart is {number}')
)
def step_impl(browser, number):
    assert ProductDetailPage.get_number_of_items_in_cart() == number

@then('he can proceed to the checkout page')
def step_impl(browser):
    pass