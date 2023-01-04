from behave import *

from pages.catalog_page import CatalogPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_overview_page import CartOverviewPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


@given('Bob has an empty shopping cart')
def step_impl(context):
    pass


@when('he adds two backpacks to the cart')
def step_impl(context):
    CatalogPage(context.appium_driver).select_first_product()
    ProductDetailPage(context.appium_driver).add_items_to_cart()


@then('the number of items in his shopping cart is {number_of_items}')
def step_impl(context, number_of_items):
    assert ProductDetailPage(context.appium_driver).get_number_of_items_in_cart() == number_of_items


@then('he can proceed to the checkout page')
def step_impl(context):
    ProductDetailPage(context.appium_driver).open_cart()
    CartOverviewPage(context.appium_driver).proceed_to_checkout()
    LoginPage(context.appium_driver).login_as('bob@example.com', '10203040')
    assert CheckoutPage(context.appium_driver).is_loaded() is True
