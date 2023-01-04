import uuid

from appium import webdriver
from behave import fixture, use_fixture


@fixture
def browser_appium(context):
    # -- SETUP-FIXTURE PART:
    caps = {}
    caps['platformName'] = 'Android'
    caps['appium:app'] = 'storage:filename=Android-MyDemoAppRN.1.3.0.build-244.apk'  # The filename of the mobile app
    caps['appium:deviceName'] = 'Google Pixel 6 Pro GoogleAPI Emulator'
    caps['appium:platformVersion'] = '12.0'
    caps['appium:automationName'] = 'UiAutomator2'
    caps['sauce:options'] = {}
    caps['sauce:options']['appiumVersion'] = '1.22.1'
    caps['sauce:options']['build'] = str(uuid.uuid4())
    caps['sauce:options']['name'] = 'Let us test this configuration'

    url = "https://basdijkstra:22105028-d602-4896-b824-d522da578fa9@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    context.appium_driver = webdriver.Remote(url, caps)
    yield context.appium_driver
    context.appium_driver.quit()


def before_tag(context, tag):
    if tag == 'fixture.appium':
        use_fixture(browser_appium, context)
