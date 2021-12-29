#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from sys import path

path.append('..')  # setting this to make possible to run test files without Pycharm e.g. from cmd.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from pages.ZalandoPage import ZalandoPage


class TestZalandoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.zalando_page = ZalandoPage(self.driver)
        self.zalando_page.driver.get(self.zalando_page.PAGE_URL)

    def test_corect_loading_page(self):
        self.assertEqual("Newsletter", self.zalando_page.get_title("Newsletter"))  # check if title is correct

        self.assertTrue(self.zalando_page.is_visible(self.zalando_page.EMAIL_PASS))  # check if elements are visible
        self.assertTrue(self.zalando_page.is_visible(self.zalando_page.FASHION_PASS))
        self.assertTrue(self.zalando_page.is_visible(self.zalando_page.SAVEME_PASS))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
