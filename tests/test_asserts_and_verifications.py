import time

import pytest
from playwright.sync_api import Playwright, expect
from smart_assertions import soft_assert, verify_expectations

my_username = "standard_user"
my_password = "secret_sauce"
expected_home_title = "Products"


class Test_Asserts_And_Verifications:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()

        yield
        time.sleep(5)
        context.close()
        page.close()

    def setup_method(self):
        page.goto("https://www.saucedemo.com/")

    def test_verify_login(self):
        # Sign in to Sauce Demo:
        page.locator("#user-name").fill(my_username)
        page.locator("#password").fill(my_password)
        page.locator("#login-button").click()
        # Verify Login is successfully
        actual_home_title = page.locator(".title").inner_text()
        print(f"\n{actual_home_title}")
        assert actual_home_title == expected_home_title

    def test_verify_login_button(self):
        login_button = page.locator("#login-button")
        print(f"Element's X Coordinate: {login_button.bounding_box()['x']}")
        print(f"Element's Y Coordinate: {login_button.bounding_box()['y']}")
        print(f"Elements Width: {login_button.bounding_box()['width']}")
        print(f"Element's Height: {login_button.bounding_box()['height']}")
        soft_assert(login_button.is_visible())
        soft_assert(login_button.is_enabled())
        verify_expectations()
