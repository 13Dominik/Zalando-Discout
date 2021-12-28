#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import path

path.append('..') # adding it to make posssible run script without PyCharm e.g. from cmd

from pages.BasePage import BasePage


class ZalandoPage(BasePage):
    PAGE_URL = "https://www.zalando.pl/zalando-newsletter/"

    def __init__(self, driver):
        super().__init__(driver)
