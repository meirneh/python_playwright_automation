import allure
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step("Verify two values are equal")
    def verify_equals(actual, expected):
        assert actual, expected

    @staticmethod
    @allure.step("Verify prices")
    def verify_items(prices, expected_min):
        for price in prices:
            soft_assert(price > expected_min, f' {price} is less than {expected_min}')
        verify_expectations()
