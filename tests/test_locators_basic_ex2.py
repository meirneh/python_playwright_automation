import time

import pytest
from playwright.sync_api import Playwright


class Test_Locators_Basic_Ex2:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.wikipedia.org/")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test01_locate_elements(self):
        ball_logo = page.locator(".central-featured-logo")
        search_bar = page.locator("#search-form")
        language_selector = page.locator("#searchLanguage")
        foot_note = page.locator("footer .footer-sidebar-text.jsl10n")
        items = []
        for locator in [ball_logo, search_bar, language_selector, foot_note]:  items.append(locator)
        for item in items:
            print(item)
        print(items)
