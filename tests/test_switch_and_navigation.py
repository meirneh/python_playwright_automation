import time


import pytest
from playwright.sync_api import Playwright


class Test_Switch_And_Navigation:
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

    def handle_alert(self, dialog):
        print("Alert Text is: ", dialog.message)
        dialog.accept()

    def test_verify_alert(self):
        page.goto(" https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        ifrm = page.frame_locator("iframe[id='iframeResult']")
        page.once("dialog", lambda dialog: self.handle_alert(dialog))
        ifrm.locator("button[onclick='myFunction()']").click()
        assert ifrm.locator("button[onclick='myFunction()']").is_visible()

    def test_verify_tab(self):
        page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open")
        ifrm = page.frame_locator("iframe[id='iframeResult']")
        ifrm.locator("button[onclick='myFunction()']").click()
        tabs = context.pages
        print("\n")
        print(f"Original Tab title: {tabs[0].title()}")
        print(f"Original Tab new title: {tabs[1].title()}")
        new_tab_title = tabs[1].title()
        assert new_tab_title == "W3Schools Online Web Tutorials"
        tabs[1].close()

