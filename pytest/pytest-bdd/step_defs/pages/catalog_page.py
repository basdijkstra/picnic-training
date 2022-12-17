from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CatalogPage(BasePage):

    def __init__(self, appium_driver):
        super().__init__(appium_driver)
        self._first_item_in_catalog: tuple = (By.XPATH, '(//android.view.ViewGroup[@content-desc="store item"])[1]')

    def select_first_product(self):
        self.click(self._first_item_in_catalog)
