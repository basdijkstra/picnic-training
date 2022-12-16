import uuid
import pytest
from appium import webdriver
from pages.catalog_page import CatalogPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_overview_page import CartOverviewPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def appium_driver():
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


def test_purchase_two_backpacks(appium_driver):

    # DONE: Go to the backpack item details
    CatalogPage(appium_driver).select_first_product()

    # We want to order two backpacks, so tap the '+' button
    # Add our two backpacks to the cart
    pdp = ProductDetailPage(appium_driver)
    pdp.add_items_to_cart()
    assert pdp.get_number_of_items_in_cart() == '2'

    # Click on the shopping cart icon to start the checkout process
    pdp.open_cart()

    # Click on the Proceed to checkout button
    CartOverviewPage(appium_driver).proceed_to_checkout()

    # Login using existing user credentials
    LoginPage(appium_driver).login_as('bob@example.com', '10203040')

    # assert that we're on the checkout screen
    assert CheckoutPage(appium_driver).is_loaded() is True
