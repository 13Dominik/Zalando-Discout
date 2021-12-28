#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """ Base class for all pages. Contains some basic methods for all pages"""
    MAX_WAIT = 10  # maximum wait 10 second to find/get something

    def __init__(self, driver):
        self.driver = driver

    def is_visible(self, by_locator) -> bool:
        """ Return True if element is visible"""
        element = WebDriverWait(self.driver, self.MAX_WAIT).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_element_text(self, by_locator) -> str:
        """ Returns string from element """
        element = WebDriverWait(self.driver, self.MAX_WAIT).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title) -> str:
        """ Return title of page """
        WebDriverWait(self.driver, self.MAX_WAIT).until(EC.title_is(title))
        return self.driver.title

    def do_click(self, by_locator) -> None:
        """ Click element """
        WebDriverWait(self.driver, self.MAX_WAIT).until(EC.visibility_of_element_located(by_locator)).click()
        return None

    def do_send_keys(self, by_locator, text) -> None:
        """ Send keys to element """
        WebDriverWait(self.driver, self.MAX_WAIT).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        return None
