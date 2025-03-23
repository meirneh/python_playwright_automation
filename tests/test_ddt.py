import csv
import time

import pytest
from playwright.sync_api import Playwright

def get_data_from_csv():
    list = []
    with open(r"C:\Users\97250\Documents\PlaywrightPython\Digital\test_automation\tests\urls.csv",newline='') as f:
        reader = csv.reader(f)
        list = [tuple(row) for row in reader]
    return list


keys = "url, expected_title"
data = [
    ("https://www.google.com", "Google"),
    ("https://www.imdb.com", "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"),
    ("https://www.bing.com", 'Search - Microsoft Bing'),
    ("https://www.instagram.com", "Instagram")
]


class Test_DDT_URL:
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

    @pytest.mark.parametrize(keys, get_data_from_csv())
    def test_login(self, url, expected_title):
        page.goto(url)
        actual_title = page.title()
        print(f"\nTITLE = {actual_title}")
        assert page.title() == expected_title
