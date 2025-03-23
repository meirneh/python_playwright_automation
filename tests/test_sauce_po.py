import allure
import pytest

from tests import base
from playwright_automation.sauce_pages import conftest
from tests.verifications import Verifications
from playwright_automation.sauce_pages.conftest import *


@pytest.mark.usefixtures("init_sauce")
class Test_Sauce_Demo:

    @allure.title("Sauce Demo - Verify Login")
    @allure.description("This test verify login is successfully")
    def test01_login(self):
        actual_home_header =base.home.get_home_page_header()
        print(f"\nThe title is: {actual_home_header}")
        Verifications.verify_equals(actual_home_header, conftest.get_data_from_xml("EXPECTED_HOME_HEADER"))
        # Verifications.verify_equals(actual_home_header, "Products")

    @allure.title("Sauce Demo - Verify Total Products")
    @allure.description("This test verify the total products is as expected")
    def test02_total_products(self):
        base.home.print_items()
        Verifications.verify_equals(base.home.get_items_total(), conftest.get_data_from_xml("EXPECTED_ITEMS_TOTAL"))

    @allure.title("Sauce Demo - Verify Prices")
    @allure.description("This test verify each price is less than expected price ")
    def test03_items_prices(self):
        prices = base.home.get_items_prices()
        Verifications.verify_items(prices, int(conftest.get_data_from_xml("EXPECTED_MINIMUM_PRICE")))
