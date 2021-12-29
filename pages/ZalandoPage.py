#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import path

path.append('..')  # adding it to make posssible run script without PyCharm e.g. from cmd

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ZalandoPage(BasePage):
    PAGE_URL = "https://www.zalando.pl/zalando-newsletter/"

    EMAIL_PASS = (
        By.XPATH, """/html/body/div[4]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[1]/div/div/input""")
    FASHION_PASS = (
        By.XPATH,
        """/html/body/div[4]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div/div[2]/div/label""")
    SAVEME_PASS = (By.XPATH, """/html/body/div[4]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[5]/button""")

    def __init__(self, driver):
        super().__init__(driver)

    def pass_email(self, email) -> None:
        self.do_send_keys(self.EMAIL_PASS, email)

    def click_fashion(self) -> None:
        self.do_click(self.FASHION_PASS)

    def click_save(self) -> None:
        self.do_click(self.SAVEME_PASS)
