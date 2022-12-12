import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

# Exercise 2.1
# Copy the required settings from the previous exercise into this fixture
# (or remove this one if the conftest.py worked for you)

@pytest.fixture
def appium_driver():
    caps = {
        # COPY FROM THE PREVIOUS EXERCISE
    }

    url = 'COPY FROM THE PREVIOUS EXERCISE'
    driver = webdriver.Remote(url, caps)
    yield driver
    driver.quit()

# Exercise 2.2
# Complete the test by completing all the steps in the test
# For now, it's OK to put time.sleep(5) between steps to make sure
# that the app loading times are dealt with. We'll work on that soon :)

def test_purchase_two_backpacks(appium_driver):

    time.sleep(10)

    # DONE: Go to the backpack item details
    xpath_backpack = '(//android.view.ViewGroup[@content-desc="store item"])[1]'
    appium_driver.find_element(By.XPATH, xpath_backpack).click()

    time.sleep(5)

    # DONE: We want to order two backpacks, so tap the '+' button
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'counter plus button').click()

    time.sleep(5)

    # DONE: Add our two backpacks to the cart
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button').click()

    time.sleep(5)

    # TO DO: Can you find out how to click the device 'Back' button?

    # TO DO: Check that the number of items in the cart is equal to 2
    xpath_number_of_items_in_cart = '//android.view.ViewGroup[@content-desc="cart badge"]/android.widget.TextView'

    # TO DO: Click on the shopping cart icon to start the checkout process
    # a11y ID: cart badge

    # TO DO: Click on the Proceed to checkout button
    # a11y ID: Proceed To Checkout button

    # TO DO: fill in username bob@example.com
    # a11y ID: Username input field

    # TO DO: fill in password 10203040
    # a11y ID: Password input field

    # TO DO: Click on the Login button
    # a11y ID: Login button

    # TO DO: assert that we're on the checkout screen
    # a11y ID: checkout address screen
