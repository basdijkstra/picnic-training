from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, appium_driver):
        super().__init__(appium_driver)
        self._screen = (AppiumBy.ACCESSIBILITY_ID, 'checkout address screen')

    def is_loaded(self):
        return self.is_visible(self._screen)
