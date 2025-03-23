import time

import pytest
from playwright.sync_api import Playwright


class Test_Locator_Basic:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        yield
        # time.sleep(5)
        context.close()
        page.close()

    def test_locators_basic(self):
        swag_header = page.locator("[class='login_logo']")
        username_field = page.locator("[id='user-name']")
        password_field = page.locator("[id='password']")
        login_button = page.locator("[id='login-button']")
        items = []
        items.append(swag_header)
        items.append(username_field)
        items.append(password_field)
        items.append(login_button)
        for item in items:
            print(item)
        links = page.locator("a")
        total_links = links.count()
        print(total_links)
        for i in range(total_links):
            print(links.nth(i))




