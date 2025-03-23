import allure
from playwright.sync_api import Page


class Webdriver_Login_Page:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = self.page.locator("#username2")
        self.password_field = self.page.locator("#password2")
        self.submit_button = self.page.locator("#submit")

    @allure.step("login with provided credentials")
    def sign_in(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
