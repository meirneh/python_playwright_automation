import xml.etree.ElementTree as ET
import pytest
from playwright.sync_api import Playwright


def get_data(node_name):
    root = ET.parse("configuration.xml").getroot()
    return root.find(".//" + node_name).text


class Test_External_Files:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        # Running browser in slow motion, in order to see the execution of the tests
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(15000)  # Set default time out for current page
        page.goto(get_data("URL"))

    def teardown_class(cls):
        context.close()
        browser.close()

    def test_verify_bmi(self):
        page.locator("[id='weight']").fill(get_data("WEIGHT"))
        page.locator("[name='height']").fill(get_data("HEIGHT"))
        page.locator("[id='calculate_data']").click()
        actual_result = page.locator("[id='bmi_result']").input_value()
        assert actual_result == get_data("EXPECTED_BMI")
