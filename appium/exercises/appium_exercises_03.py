import time
import uuid

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

# Exercise 3.1
# Copy the required settings from the previous exercise into this fixture
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture
def appium_driver():
    caps = {
        # COPY FROM THE PREVIOUS EXERCISE
    }

    url = 'COPY FROM THE PREVIOUS EXERCISE'
    driver = webdriver.Remote(url, caps)
    yield driver
    driver.quit()

# Exercise 3.2
# Improve our test code by replacing all the time.sleep(5) statements
# with explicit waits. Make sure you wait for the right element state!

# Exercise 3.3
# Extract the synchronization into helper methods for improved reusability


def test_purchase_two_backpacks(appium_driver):

    time.sleep(10)

    # DONE: Go to the backpack item details
    xpath_backpack = '(//android.view.ViewGroup[@content-desc="store item"])[1]'
    WebDriverWait(appium_driver, 120).until(ec.element_to_be_clickable((AppiumBy.XPATH, xpath_backpack)))
    appium_driver.find_element(AppiumBy.XPATH, xpath_backpack).click()

    time.sleep(5)

    # We want to order two backpacks, so tap the '+' button
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'counter plus button').click()

    time.sleep(5)

    # Add our two backpacks to the cart
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button').click()

    time.sleep(5)

    # Can you find out how to click the device 'Back' button?
    appium_driver.back()

    time.sleep(5)

    # Check that the number of items in the cart is equal to 2
    xpath_number_of_items_in_cart = '//android.view.ViewGroup[@content-desc="cart badge"]/android.widget.TextView'
    assert appium_driver.find_element(By.XPATH, xpath_number_of_items_in_cart).text == '2'

    time.sleep(5)

    # Click on the shopping cart icon to start the checkout process
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'cart badge').click()

    time.sleep(5)

    # Click on the Proceed to checkout button
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Proceed To Checkout button').click()

    time.sleep(5)

    # fill in username bob@example.com
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Username input field').send_keys('bob@example.com')

    time.sleep(5)

    #  fill in password 10203040
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Password input field').send_keys('10203040')

    time.sleep(5)

    # Click on the Login button
    appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Login button').click()

    time.sleep(5)

    # assert that we're on the checkout screen
    assert appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'checkout address screen').is_displayed() is True
