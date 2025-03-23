import csv
import time

import pytest
from playwright.sync_api import Playwright


def get_data_from_csv():
    list = []
    with open(r"C:\Users\97250\Documents\PlaywrightPython\Digital\test_automation\tests\bmi.csv", newline='') as f:
        reader = csv.reader(f)
        list = [tuple(row) for row in reader]
    return list


keys = "weight, height, expected_bmi"


class Test_Data_BMI:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/bmi/")

        yield
        time.sleep(5)
        context.close()
        page.close()

    @pytest.mark.parametrize(keys, get_data_from_csv())
    def test_bmi(self, weight, height, expected_bmi):
        page.locator("#weight").fill(weight)
        page.locator("#hight").fill(height)
        page.locator("#calculate_data").click()
        actual_bmi = page.locator("#bmi_result").input_value()
        page.locator("#reset_data").click()
        assert actual_bmi == expected_bmi
