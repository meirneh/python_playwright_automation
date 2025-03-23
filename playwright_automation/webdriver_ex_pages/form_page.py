from playwright.sync_api import Page


class Form_Page:
    def __init__(self, page: Page):
        self.page = page
        self.occupation_field = self.page.locator("#occupation")
        self.age_field = self.page.locator("#age")
        self.location_field = self.page.locator("#location")
        self.button = self.page.locator("#form button")

    def fill_form(self, occupation, age, location):
        self.occupation_field.fill(occupation)
        self.age_field.fill(age)
        self.location_field.fill(location)
        self.button.click()
