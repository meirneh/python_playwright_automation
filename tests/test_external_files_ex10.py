import time

import pytest
from playwright.sync_api import Playwright
import xml.etree.ElementTree as ET


def get_data_from_xml(node_name):
    root = ET.parse(r"/tests/playwright_automation/bmi_data.xml").getroot()
    node = root.find(f".//{node_name}")
    return node.text.strip() if node is not None and node.text else ""


my_weight = get_data_from_xml("MY_WEIGHT")
my_height = get_data_from_xml("MY_HEIGHT")
my_BMI = get_data_from_xml("MY_BMI")
my_message = get_data_from_xml("MY_MESSAGE")
empty_value = get_data_from_xml("EMPTY_VALUE")
text_button = get_data_from_xml("TEXT_BUTTON")
expected_error_message = get_data_from_xml("EXPECTED_ERROR_MESSAGE")


class Test_Assert_And_Verifications_Ex1:
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
        # browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        # page.goto(get_data_from_xml("URL"))

        yield
        time.sleep(5)
        context.close()
        page.close()

    def setup_method(self):
        page.goto(get_data_from_xml("URL"))

    def test01_result_verification(self):
        page.locator("#weight").fill(my_weight)
        page.locator("#hight").fill(my_height)
        page.locator("#calculate_data").click()
        assert page.locator("#bmi_result").input_value() == my_BMI
        print(f"\nBMI MESSAGE: {page.locator('#bmi_means').input_value()}")
        assert page.locator('#bmi_means').input_value() == my_message
        page.locator("#reset_data").click()
        assert page.locator("#weight").input_value() == empty_value
        assert page.locator("#hight").input_value() == empty_value

    def test02_inspect_calculateBMIButton(self):
        calculate_button = page.locator("#calculate_data")
        print(f"Element's X Coordinate: {calculate_button.bounding_box()['x']}")
        print(f"Element's Y Coordinate: {calculate_button.bounding_box()['y']}")
        print(f"Elements Width: {calculate_button.bounding_box()['width']}")
        print(f"Element's Height: {calculate_button.bounding_box()['height']}")
        assert calculate_button.is_enabled()
        assert calculate_button.is_visible()
        print(f"\nValue on the Button: {calculate_button.get_attribute('value')}")
        assert calculate_button.get_attribute('value') == text_button
        assert not page.locator('#validation').is_visible()
        calculate_button.click()
        actual_error_message = page.locator('#validation').inner_text()
        assert page.locator('#validation').is_visible()
        print(f"ERROR MESSAGE: {actual_error_message}")
        assert actual_error_message == expected_error_message
