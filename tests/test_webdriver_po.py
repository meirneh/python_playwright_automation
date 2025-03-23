import time

import pytest
from playwright.sync_api import Playwright

from playwright_automation.webdriver_ex_pages.click_page import Click_Page
from playwright_automation.webdriver_ex_pages.form_page import Form_Page
from playwright_automation.webdriver_ex_pages.webdriver_login_page import Webdriver_Login_Page

username = "selenium"
password = "webdriver"
occupation = "QA Engineer"
age = "61"
location = "Revadim"


class Test_Webdriver_PO:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, login, form_page, click_page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/webdriveradvance.html")
        # init page objects
        login = Webdriver_Login_Page(page)
        form_page = Form_Page(page)
        click_page = Click_Page(page)

        yield
        time.sleep(5)
        context.close()
        page.close()

    def test01_login(self):
        login.sign_in(username, password)
        form_page.fill_form(occupation, age, location)
        click_page.clickButton()
        print(page.url)


