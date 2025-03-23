import time

import playwright
import pytest
from playwright.sync_api import Playwright


class Test_Driver_Connection_Ex3:
    def test_drivers(self,playwright: Playwright):
        # Chrome
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com/")
        page.close()
        # Edge
        browser = playwright.chromium.launch(headless=False, channel="msedge")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com/")
        page.close()
        # FireFox
        browser = playwright.firefox.launch(headless=False, channel="firefox")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com/")
        page.close()