import time

import pytest
from playwright.sync_api import Playwright


class Test_Actions:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://marcojakob.github.io/dart-dnd/basic/")

        yield
        time.sleep(5)
        context.close()
        page.close()

    def test_drag_and_drop(self):
        paper = ".container > img:nth-child(3)"
        trash_can = ".container .trash"
        page.drag_and_drop(paper, trash_can, force=True)
        assert page.locator(trash_can).get_attribute("class") == "trash full"

