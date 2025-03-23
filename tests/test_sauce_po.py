import allure
import pytest
from tests.verifications import Verifications


@pytest.mark.usefixtures("init_sauce")
class Test_Sauce_Demo:

    @allure.title("Sauce Demo - Verify Login")
    @allure.description("This test verify login is successfully")
    def test01_login(self):
        actual_home_header = self.home.get_home_page_header()
        print(f"\nThe title is: {actual_home_header}")
        Verifications.verify_equals(actual_home_header, self.expected_home_header)

    @allure.title("Sauce Demo - Verify Total Products")
    @allure.description("This test verify the total products is as expected")
    def test02_total_products(self):
        self.home.print_items()
        Verifications.verify_equals(self.home.get_items_total(), self.expected_items_total)

    @allure.title("Sauce Demo - Verify Prices")
    @allure.description("This test verify each price is less than expected price ")
    def test03_items_prices(self):
        prices = self.home.get_items_prices()
        Verifications.verify_items(prices, self.expected_minimum_price)
