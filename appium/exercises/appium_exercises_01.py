import pytest
from appium import webdriver

# Exercise 1
# Use the SauceLabs configurator to get the capabilities to
# start a session on an Android GoogleAPI Emulator device,
# with the SauceLabs demo app loaded. Also supply useful values
# for the build and test names. Run your test to see if it works.

@pytest.fixture
def driver():
    caps = {
        # GET THESE FROM SAUCELABS
    }

    url = 'GET THIS FROM SAUCELABS'
    driver = webdriver.Remote(url, caps)
    yield driver
    driver.quit()


def test_connectivity(driver):
    pass