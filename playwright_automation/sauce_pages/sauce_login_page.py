import allure
from playwright.sync_api import Page


class SauceLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_name_field = self.page.locator("#user-name")
        self.password_field = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")

    @allure.step("Sign in using provided credentials")
    def sign_in(self, username, password):
        self.user_name_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()




