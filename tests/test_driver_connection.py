import time

import pytest
from playwright.sync_api import Playwright

expected_title = "Google"


class Test_Driver_Connection:

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

    def test01_verify_title(self):
        actual_title = page.title()
        if actual_title == expected_title:
            print("Test Passed")
        else:
            print("Test failed")
            print(f"This title is: {actual_title}")
        page.goto("https://www.imdb.com")
        page.reload()
        print(f"URL is: {page.url}")
        page.go_back()
        page.go_back()
