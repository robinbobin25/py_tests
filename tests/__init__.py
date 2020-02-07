import pytest
from my_sum import sum
from selenium import webdriver


class TestSum:

    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"
        print("pass 1")

    def test_sum_tuple(self):
        assert sum((1, 2, 3)) == 6, "Should be 6"
        print("pass 2")
