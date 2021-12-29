import unittest
from sys import path
import re

path.append('..')  # adding it to make posssible run tests without PyCharm e.g. from cmd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from pages.EmailPage import EmailPage


class TestEmailPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.email_page = EmailPage(self.driver)
        self.email_page.driver.get(self.email_page.PAGE_URL)

    def test_corect_loading_page(self):
        self.assertEqual("10-minutowy Mail", self.email_page.get_title("10-minutowy Mail"))  # check if title is correct

        self.assertTrue(self.email_page.is_visible(self.email_page.NEW_EMAIL_LABEL))  # check if email label is visible

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.assertTrue(re.fullmatch(regex, self.email_page.get_email()))  # check if coping email works

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
