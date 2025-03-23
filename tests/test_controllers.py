import time

import pytest
from playwright.sync_api import Playwright

my_name = "Meir Nehemkin"
my_subject = "Tank You"
my_email = "meir@gmail.com"
my_message = "It was amazing"


class Test_Controllers:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atid.store/")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test_01_controllers(self):
        page.locator("#menu-item-45").click()
        my_selector = ".orderby"
        page.select_option(my_selector, value="price")
        time.sleep(2)
        items = page.locator(".woocommerce-loop-product__title")
        for item in range(items.count()):
            print(f"\n{item + 1} => {items.nth(item).inner_text()}")
        page.locator("#menu-item-829").click()
        page.locator("#wpforms-15-field_0").fill(my_name)
        page.locator("#wpforms-15-field_5").fill(my_subject)
        page.locator("#wpforms-15-field_4").fill(my_email)
        page.locator("#wpforms-15-field_2").fill(my_message)
        page.locator("#wpforms-submit-15").click()
