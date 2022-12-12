import pytest
from appium import webdriver

# Exercise 1
# Use the SauceLabs configurator to get the capabilities to
# start a session on an Android GoogleAPI Emulator device,
# with the SauceLabs demo app loaded. Also supply useful values
# for the build and test names. Run your test to see if it works.

# Exercise 2
# Move the fixture to a separate file conftest.py in the 'exercises' folder
# This should make the fixture available to all modules, saving us from
# having to copy and paste it in all exercises.
# Test if this still works!

@pytest.fixture
def driver():
    caps = {
        # GET THESE FROM SAUCELABS
        # REMOVE THE DEVICE NAME
        # TO INCREASE CHANCES OF FINDING AN AVAILABLE DEVICE
    }

    url = 'GET THIS FROM SAUCELABS'
    driver = webdriver.Remote(url, caps)
    yield driver
    driver.quit()


def test_connectivity(driver):
    pass