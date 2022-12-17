from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductDetailPage(BasePage):

    def __init__(self, appium_driver):
        super().__init__(appium_driver)
        self._increase_button = (AppiumBy.ACCESSIBILITY_ID, 'counter plus button')
        self._add_to_cart_button = (AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button')

    def add_items_to_cart(self):
        self.click(self._increase_button)
        self.click(self._add_to_cart_button)

