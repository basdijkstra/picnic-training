import time
import uuid

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture
def driver():
    caps = {
        'platformName': 'Android',
        'appium:app': 'storage:filename=Android-MyDemoAppRN.1.3.0.build-244.apk',
        'appium:automationName': 'UiAutomator2',
        'sauce:options': {
            'appiumVersion': '1.22.1',
            'build': str(uuid.uuid4()),
            'name': 'Connectivity test'
        }
    }

    url = 'https://basdijkstra:22105028-d602-4896-b824-d522da578fa9@ondemand.eu-central-1.saucelabs.com:443/wd/hub'
    driver = webdriver.Remote(url, caps)
    yield driver
    driver.quit()


def test_connectivity(driver):
    pass


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
