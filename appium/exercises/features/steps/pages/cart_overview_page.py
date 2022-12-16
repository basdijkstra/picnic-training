from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CartOverviewPage(BasePage):

    def __init__(self, appium_driver):
        super().__init__(appium_driver)
        self._proceed_to_checkout = (AppiumBy.ACCESSIBILITY_ID, 'Proceed To Checkout button')

    def proceed_to_checkout(self):
        self.click(self._proceed_to_checkout)
