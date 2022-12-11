import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture
def appium_driver():
    caps = {
        'platformName': "Android",
        # 'appium:deviceName': "Android GoogleAPI Emulator",
        'appium:deviceName': "emulator-5554",
        'appium:platformVersion': "10.0",
        'appium:automationName': "UiAutomator2",
        # 'appium:app': "Android-MyDemoAppRN.1.3.0.build-244.apk",
        # 'sauce:options': {
        #     'build': 'Test build',
        #     'name': 'Yet another demo test'
        # }
    }

    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, caps)
    yield driver
    driver.quit()


def test_connectivity(appium_driver):

    # appium_driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'open menu').click()
    appium_driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="store item"])[1]').click()


def naive_wait_and_click():
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@content-desc="open menu"]/android.widget.ImageView').click()


def use_explicit_wait_before_click():
    locator = (By.XPATH, '//*[@content-desc="open menu"]/android.widget.ImageView')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).click()


def use_helper_method_to_click():
    click(locator=(By.XPATH, '//*[@content-desc="open menu"]/android.widget.ImageView'))


def click(locator):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).click()
