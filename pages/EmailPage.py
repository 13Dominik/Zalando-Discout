#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import path

from selenium.webdriver.common.by import By

path.append('..')

from pages.BasePage import BasePage


class EmailPage(BasePage):
    PAGE_URL = "https://10minutemail.net/?lang=pl"

    NEW_EMAIL_LABEL = (By.XPATH, "/html/body/div[1]/div[3]/div[5]/div[2]/button")

    def __init__(self, driver):
        super().__init__(driver)