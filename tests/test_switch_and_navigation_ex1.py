import time

import pytest
from playwright.sync_api import Playwright

iframe_text = '\n\n\nThis is an IFrame !'


class Test_Switch_And_Navigation_Ex1:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=400)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_switch_navigation.html")

        yield
        time.sleep(5)
        context.close()
        page.close()

    def handle_alert(self, dialog):
        print("Alert Text is: ", dialog.message)
        dialog.accept()

    def handle_prompt(self, dialog, text):
        print(f"Hi, What's Your Name ? {dialog.message}")
        dialog.accept(text)

    def test01_verify_Alert(self):
        page.once("dialog", lambda dialog: self.handle_alert(dialog))
        page.locator("#btnAlert").click()
        assert page.locator("#output").inner_text() == "Alert is gone."

    def test02_verify_alert_prompt(self):
        page.once("dialog", lambda dialog: self.handle_prompt(dialog, "Meir"))
        page.locator("#btnPrompt").click()
        assert page.locator("#output").inner_text() == "Meir"

    def test03_verify_Ifrsme(self):
        ifrm = page.frame_locator("[src='ex_switch_newFrame.html']")
        print(f"The text inside of the iframe is: {ifrm.locator('#iframe_container').inner_text()}")
        assert ifrm.locator('#iframe_container').inner_text() == iframe_text

    def test04_verify_tab(self):
        page.locator("#btnNewTab").click()
        tabs = context.pages
        print("\n")
        print(f"Original Tab title: {tabs[0].title()}")
        assert tabs[0].title() == "Switch N Navigation | Atid College"
        tabs[1].close()

    def test05_verify_windows(self):
        page.locator("#contact_info_left  a").click()
        windows = context.pages
        text_windows = windows[1].locator('#new_window_container').inner_text()
        print("\n")
        print(f"Original Window title: {text_windows}")
        assert text_windows == "\n\n\nThis is a new window"
        windows[1].close()
