from playwright.sync_api import Page


class Click_Page:
    def __init__(self, page: Page):
        self.page = page
        self.clik_me_button = self.page.locator("tr:nth-child(2) td button")

    def clickButton(self):
        self.clik_me_button.click()