import time

import pytest
from playwright.sync_api import Playwright


class Test_Locators_Advanced_Ex1:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_locators.html")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test01_locate_and_print_elements(self):
        element1 = page.locator("#locator_id")
        element2 = page.locator("[name='locator_name']")
        element3 = page.locator("#contact_info_left  p")
        element4 = page.locator(".locator_class")
        element5 = page.locator("a:nth-child(12)")
        element6 = page.locator("a:nth-child(15)")
        element7 = page.locator("[myname='selenium']")
        element8 = page.locator("#contact_info_left  button")
        print(f"\nThe element n1 is: {element1}")
        print(f"The element n2 is {element2}")
        print(f"The element n3 is {element3}")
        print(f"The element n4 is {element4}")
        print(f"The element n5 is {element5}")
        print(f"The element n6 is {element6}")
        print(f"The element n7 is {element7}")
        print(f"The element n8 is {element8}")

    def test02_locate_and_print_elements_text(self):
        element1 = page.locator("#locator_id")
        element2 = page.locator("[name='locator_name']")
        element3 = page.locator("#contact_info_left  p")
        element4 = page.locator(".locator_class")
        element5 = page.locator("a:nth-child(12)")
        element6 = page.locator("a:nth-child(15)")
        element7 = page.locator("[myname='selenium']")
        element8 = page.locator("#contact_info_left  button")
        print(f"\nThe element n1 is: {element1.inner_text()}")
        print(f"The element n2 is {element2.inner_text()}")
        print(f"The element n3 is {element3.inner_text()}")
        print(f"The element n4 is {element4.inner_text()}")
        print(f"The element n5 is {element5.inner_text()}")
        print(f"The element n6 is {element6.inner_text()}")
        print(f"The element n7 is {element7.inner_text()}")
        print(f"The element n8 is {element8.inner_text()}")


