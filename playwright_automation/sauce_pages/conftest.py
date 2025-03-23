import time

import allure
import pytest
from playwright.sync_api import Playwright

from playwright_automation.sauce_pages.sauce_home_page import SauceHomePage
from playwright_automation.sauce_pages.sauce_login_page import SauceLoginPage
from tests import base
import xml.etree.ElementTree as ET


@pytest.fixture(scope="class", autouse=True)
def init_sauce(request, playwright: Playwright):
    browser_type = get_data_from_xml("BROWSER_TYPE").lower()
    slow_motion = int(get_data_from_xml("SLOW_MO"))
    if browser_type == "chrome":
        base.browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=slow_motion )
    elif browser_type == "edge":
        base.browser = playwright.chromium.launch(headless=False, channel="msedge", slow_mo=slow_motion)
    elif browser_type == "firefox":
        base.browser = playwright.firefox.launch(headless=False, channel="firefox", slow_mo=slow_motion)

    base.context = base.browser.new_context()
    # Start tracing before creating / navigating to page
    base.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    base.page
    base.page = base.context.new_page()
    base.page.goto("https://www.saucedemo.com/inventory.html")
    # init page objects
    base.login = SauceLoginPage(base.page)
    base.home = SauceHomePage(base.page)
    base.login.sign_in(get_data_from_xml("SAUCE_USER_NAME"), get_data_from_xml("SAUCE_PASSWORD"))

    yield
    time.sleep(5)
    base.context.tracing.stop(path="../../tests/trace.zip")
    base.context.close()
    base.page.close()


def pytest_exception_interact(node, call, report):
    if report.failed:
        # screen-shots folder must be created beforehand
        image_path = "../../tests/playwright_automation/screen-shots"
        image = base.page.screenshot(path=image_path, full_page=True)
        allure.attach.file(image_path, attachment_type=allure.attachment_type.PNG)


def get_data_from_xml(node_name):
    root = ET.parse(
        r"C:\Users\97250\Documents\PlaywrightPython\Digital\test_automation\tests\sauce_data_po.xml").getroot()
    return root.find(f".//{node_name}").text
