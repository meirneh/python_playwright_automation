import time

import allure
import pytest
from playwright.sync_api import Playwright

captain_america_user_name = "CaptainAmerica"
captain_america_password = "CaptainAmericarocks"
expected_movie_score = "6.9"


class Test_Reporting:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=300)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/workshops/avengers/exercise/")

        yield
        time.sleep(5)
        context.close()
        page.close()

    @allure.title("Captain America - Verify Score")
    @allure.description("Verify Captain America Movie Score")
    def test_verify_movie_score(self):
        try:
            self.navigate_to_captain_america()
            self.sign_in(captain_america_user_name, captain_america_password)
            self.verify_movie_score(expected_movie_score)
        except Exception as e:
            self.attache_file()
            pytest.fail("Test Failed, see details:", e)

    @allure.step("Verify Movie Score is as expected")
    def verify_movie_score(self, expected):
        actual_movie_score = page.locator(".kUfGfN :nth-child(1) .sc-d541859f-1").inner_text()
        assert actual_movie_score == expected_movie_score

    def attache_file(self):
        # screen-shots folder must be created beforehand
        image_path = "./screen-shots/screen.png"
        image = page.screenshot(image_path, full_page=True)
        allure.attach.file(image_path, attachment_type=allure.attachment_type.PNG)

    @allure.step("Sign in using provided username and password")
    def sign_in(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.submit()

    @allure.step("Enter user username")
    def enter_username(self, username):
        page.locator("#username").fill(username)

    @allure.step("Enter user password")
    def enter_password(self, password):
        page.locator("#username").fill(password)

    @allure.step("Submit Username and Password")
    def submit(self):
        page.locator("#submit").click()

    @allure.step("Navigate to Captain America Login Page")
    def navigate_to_captain_america(self):
        page.locator("body tr:nth-child(2) td:nth-child(2)").click()
