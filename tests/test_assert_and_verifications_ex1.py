import time

import pytest
from playwright.sync_api import Playwright

my_weight = "92"
my_height = "180"
my_BMI = "28"
my_message = "That you have overweight."
empty_value = ''
text_button = "Calculate BMI"
expected_error_message = "Please Fill in all fields correctly !"


class Test_Assert_And_Verifications_Ex1:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/bmi/")

        yield
        time.sleep(5)
        context.close()
        page.close()



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




