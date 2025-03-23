import pytest


class Test_Example:
    def setup_class(self):
        print("\nBefore all - This will run before once anything")

    def teardown_class(self):
        print("\nAfter all - This will run after once anything")

    def setup_method(self):
        print("\nBefore Each - This will run before each test")

    def teardown_method(self):
        print("\nAfter Each - This will run after each test")


    def test_01_something(self):
        print("\nTest01 - Something")

    def test_02_something(self):
        print("\nTest02 - Something")
