import time

import allure
import pytest
from playwright.sync_api import Playwright

from playwright_automation.sauce_pages.sauce_home_page import SauceHomePage
from playwright_automation.sauce_pages.sauce_login_page import SauceLoginPage

sauce_username = "standard_user"
sauce_password = "secret_sauce"
expected_home_header = "Products"
expected_items_total = 6
expected_minimum_price = 10


@pytest.fixture(scope="class", autouse=True)
def init_sauce(request, playwright: Playwright):
    # global browser, context, page, login, home
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    context = browser.new_context()
    # Start tracing before creating / navigating to page
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    global page
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    # init page objects
    login = SauceLoginPage(page)
    home = SauceHomePage(page)
    login.sign_in(sauce_username, sauce_password)
    request.cls.page = page
    request.cls.login = login
    request.cls.home = home
    request.cls.expected_home_header = expected_home_header
    request.cls.expected_items_total = expected_items_total
    request.cls.expected_minimum_price = expected_minimum_price
    yield
    time.sleep(5)
    context.tracing.stop(path="trace.zip")
    context.close()
    page.close()


def pytest_exception_interact(node, call, report):
    if report.failed:
        # screen-shots folder must be created beforehand
        image_path = "./playwright_automation/screen-shots/screen.png"
        image = page.screenshot(image_path, full_page=True)
        allure.attach.file(image_path, attachment_type=allure.attachment_type.PNG)
