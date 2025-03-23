import time

import pytest
from playwright.sync_api import Playwright, expect
import xml.etree.ElementTree as ET


def get_data_from_xml(node_name):
    root = ET.parse(r"/tests/playwright_automation/sauce_data.xml").getroot()
    return root.find(f".//{node_name}").text


my_username = get_data_from_xml("USER_NAME")
my_password = get_data_from_xml("PASSWORD")
expected_home_title = get_data_from_xml("EXPECTED_HOME_TITLE")


class Test_External_files:
    def init_browser(self, playwright: Playwright, browser_type):
        if browser_type.lower() == "chrome":
            return playwright.chromium.launch(headless=False, channel="chrome")
        elif browser_type.lower() == "firefox":
            return playwright.firefox.launch(headless=False, channel="firefox")
        elif browser_type.lower() == "edge":
            r = playwright.chromium.launch(headless=False, channel="msedege")
        else:
            pytest.fail("Error: unsupported browser type...!!!")

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = self.init_browser(playwright, get_data_from_xml("BROWSER_TYPE"))

        context = browser.new_context()
        page = context.new_page()

        yield
        time.sleep(5)
        context.close()
        page.close()

    def setup_method(self):
        page.goto(get_data_from_xml("URL"))

    def test_verify_login(self):
        # Sign in to Sauce Demo:
        page.locator("#user-name").fill(my_username)
        page.locator("#password").fill(my_password)
        page.locator("#login-button").click()
        # Verify Login is successfully
        actual_home_title = page.locator(".title").inner_text()
        print(f"\n{actual_home_title}")
        assert actual_home_title == expected_home_title
