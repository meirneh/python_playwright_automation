import time

import pytest
from playwright.sync_api import Playwright

my_username = "ironman"
my_password = "ironmanrocks"


class Test_Locators_Advanced:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/workshops/avengers/exercise/")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test_01_print_avengers(self):
        avengers = page.locator("body tr:nth-child(1) td")
        total_avengers = avengers.count()
        print(f"\nTotal avengers {total_avengers} avengers")
        for i in range(total_avengers):
            print(f"Avenger: {i + 1} => {avengers.nth(i).inner_text()}")

    def test_02_iron_man_login(self):
        page.locator("body tr:nth-child(2) td:nth-child(1)").click()
        page.locator("#username").fill(my_username)
        page.locator("#password").fill(my_password)
        page.locator("#submit").click()
