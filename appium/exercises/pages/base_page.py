from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, appium_driver):
        self._appium_driver = appium_driver
        self._number_of_items_in_cart = (By.XPATH, '//android.view.ViewGroup[@content-desc="cart badge"]/android.widget.TextView')
        self._cart_icon = (AppiumBy.ACCESSIBILITY_ID, 'cart badge')

    def click(self, locator):
        WebDriverWait(self._appium_driver, 10)\
            .until(ec.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        WebDriverWait(self._appium_driver, 10)\
            .until(ec.element_to_be_clickable(locator)).send_keys(value)

    def is_visible(self, locator):
        return WebDriverWait(self._appium_driver, 10)\
            .until(ec.visibility_of_element_located(locator)).is_displayed()

    def get_number_of_items_in_cart(self):
        return WebDriverWait(self._appium_driver, 10)\
            .until(ec.visibility_of_element_located(self._number_of_items_in_cart))\
            .text

    def open_cart(self):
        self.click(self._cart_icon)
