import time

import pytest
from playwright.sync_api import Playwright
expected_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
expected_url = "https://www.imdb.com/"


class Test_Driver_Connection_Ex1:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.imdb.com/")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test_01_verify_title(self):
        page.reload()
        actual_page = page.title()
        print(f"The title of the page is: {actual_page}")
        if actual_page == expected_title:
            print("The test is passed")
        else:
            print("the test is failed")

    def test_02_verify_url(self):
        actual_url = page.url
        print(f"The URL is: {actual_url}")
        if actual_url == expected_url:
            print("The test is passed")
        else:
            print("the test is failed")


