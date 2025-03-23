import time

import pytest
from playwright.sync_api import Playwright


class Test_Errors:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atid.store/")
        page.set_default_timeout(10 * 1000)

        yield
        time.sleep(5)
        context.close()
        page.close()

    def test_error_strict_mode(self):
        page.locator("//span").first.click()

    def test_verify_element_existence_with_try_except(self):
        try:
            page.locator("kkkkk").click()
        except Exception as e:
            print("The was an error", e)

    def test_verify_element_existence_no_try_except(self):
        items = page.locator("kkkkk")
        assert items.count() == 0




