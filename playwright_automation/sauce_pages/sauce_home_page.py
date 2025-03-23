import allure
from playwright.sync_api import Page


class SauceHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.home_page_header = self.page.locator(".title")
        self.items_titles = self.page.locator(".inventory_item_name ")
        self.items_prices = self.page.locator(".inventory_item_price")
        self.menu_button = self.page.locator("#react-burger-menu-btn")
        self.logout_button = self.page.locator("#logout_sidebar_link")

    @allure.step("logout and back to login page")
    def logout(self):
        self.menu_button.click()
        self.logout_button.click()

    @allure.step("Return the home page header text")
    def get_home_page_header(self):
        return self.home_page_header.inner_text()

    @allure.step("Print list of items")
    def print_items(self):
        for i in range(self.items_titles.count()):
            print(f"\nitem {i + 1} is {self.items_titles.nth(i).inner_text()}")

    @allure.step("Get total number of items")
    def get_items_total(self):
        return self.items_titles.count()

    @allure.step("return the item's prices")
    def get_items_prices(self):
        prices = []
        for i in range(self.items_prices.count()):
            current_item_price = self.items_prices.nth(i).inner_text()
            price = float(current_item_price.replace('$', ''))
            prices.append(price)
        return prices

