import time

import pytest
from playwright.sync_api import Playwright

firstname = "Meir"
lastname = "Nehemkin"


class Test_Controllers_Ex1:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_controllers.html")
        yield
        time.sleep(5)
        context.close()
        page.close()

    def test01_verify_controllers(self):
        page.locator("[name='firstname']").fill(firstname)
        page.locator("[name='lastname']").fill(lastname)
        page.select_option("#continents", value="europe")
        page.locator("#submit").click()
        current_url = page.url
        print(f"\n THE CURRENT URL IS: {current_url}")
        if firstname and lastname in current_url:
            print("Test Passed")
        else:
            print("Test Failed")

    def test02_verify_controllers_bonus(self):
        page.reload()
        page.locator("[name='firstname']").fill(firstname)
        page.locator("[name='lastname']").fill(lastname)
        page.locator("#sex-1").click()
        page.locator("#sex-0").click()
        years = page.locator("[id^='exp-']")
        total_years = years.count()
        print(f"\nYears of experience {total_years}")
        for year in range(total_years):
            years.nth(year).click()
        page.locator("#datepicker").click()
        dates_container = page.locator("#ui-datepicker-div")
        dates = dates_container.locator(".ui-state-default")
        for date in range(dates.count()):
            if dates.nth(date).inner_text() == "18":
                dates.nth(date).click()
                break
        page.locator("#profession-1").click()
        tools = page.locator("[id^='tool-']")
        total_tools = tools.count()
        print(f"\nAutomation tools {total_tools}")
        for tool in range(total_tools):
            tools.nth(tool).click()
        page.select_option("#continents", value="samerica")
        page.select_option("#selenium_commands", value="swithch")
        page.locator("#submit").click()
        current_url = page.url
        print(f"\n THE CURRENT URL IS: {current_url}")
        arr = current_url.split("%2F")
        print(arr)
