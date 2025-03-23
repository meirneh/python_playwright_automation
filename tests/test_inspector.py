import re
import time

import pytest
from playwright.sync_api import Page, expect, Playwright


class Test_inspector:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atid.store/")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test_example(self) -> None:
        # page.goto("https://atid.store/")
        page.get_by_role("link", name="Store").click()
        page.locator("#menu-item-829").get_by_role("link", name="Contact Us").click()
        page.get_by_role("textbox", name="Name *").click()
        page.get_by_role("textbox", name="Name *").fill("Playwright")
        page.get_by_role("textbox", name="Single Line Text").fill("Playwright - Inspector")
        page.get_by_role("textbox", name="Email *").fill("playwright@inspector.com")
        page.get_by_role("textbox", name="Comment or Message *").fill("This was recorded using playwright inspector")
        page.get_by_role("button", name="Send Message").click()
