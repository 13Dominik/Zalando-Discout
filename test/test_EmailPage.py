import unittest
from sys import path

path.append('..')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from pages.EmailPage import EmailPage

# class TestEmailPage(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#
#     def test_search_in_python_org(self):
#         email_page = EmailPage(self.driver)
#         # driver.get("http://www.python.org")
#         # self.assertIn("Python", driver.title)
#         # elem = driver.find_element_by_name("q")
#         # elem.send_keys("pycon")
#         # elem.send_keys(Keys.RETURN)
#         # assert "No results found." not in driver.page_source
#
#
#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()
