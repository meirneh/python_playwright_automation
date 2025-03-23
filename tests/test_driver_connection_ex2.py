import time

import pytest
from playwright.sync_api import Playwright


class Test_Driver_Connection_Ex2:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test_01_navigate(self):
        page.goto("https://www.bing.com/")
        print(f"\nThe title of the current page is: {page.title()}")
        page.go_back()
        print(f"The title of the current page is: {page.title()}")
        source = page.content()
        if "bubble" in source:
            print("Exist")
        else:
            print("Not exist")

