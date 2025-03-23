import time

import pytest
from playwright.sync_api import Playwright

my_user_agent = "Meir_AGENT"


class Test_Emulation_EX:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=200)
        context = browser.new_context(viewport={"width": 1280, "height": 1024},
                                      user_agent=my_user_agent, locale='es-AR',
                                      timezone_id='America/Argentina/Buenos_Aires')
        page = context.new_page()
        page.set_default_timeout(15000)
        yield
        context.close()
        browser.close()

    def test01_user_agent(self):
        page.goto("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
        print(f"\nThe user agent is: {page.locator('#detected_value').inner_text()}")
        assert page.locator('#detected_value').inner_text() == my_user_agent

    def test02_time_zone(self):
        page.goto("https://www.google.com")
        page.locator("[name='q']").fill("Time Zone")
        page.keyboard.press("Enter")
        time.sleep(5)
        page.goto("https://www.localeplanet.com/support/browser.html")
        print(f"\n LOCALE: {page.locator('body :nth-child(12)').inner_text()}")
        assert page.locator('body :nth-child(12)').inner_text() == "Locale code: es-AR"
        time.sleep(5)
