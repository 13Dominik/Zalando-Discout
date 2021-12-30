#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from sys import path

from selenium.webdriver.common.by import By
import pyperclip as pc

path.append('..')  # adding it to make posssible run script without PyCharm e.g. from cmd

from pages.BasePage import BasePage


class EmailPage(BasePage):
    PAGE_URL = "https://10minutemail.net/?lang=pl"

    NEW_EMAIL_LABEL = (By.XPATH, "/html/body/div[1]/div[3]/div[5]/div[2]/button")

    FIRST_EMAIL = (By.XPATH, """/html/body/div[1]/div[4]/div/table/tbody/tr[2]/td[1]/a""")
    CONFIRM_EMAIL_LABEL = (By.XPATH,
                           """/html/body/div[1]/div[4]/div/div/div[4]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/table[6]/tbody/tr/td/table/tbody/tr/td/table[5]/tbody/tr/td/table/tbody/tr/td/a""")

    EMAIL_WITH_CODE_VISIBLE = (By.XPATH, """/html/body/div[1]/div[5]/div/table/tbody/tr[2]/td[2]/a""")
    EMAIL_WITH_CODE = (By.XPATH, """/html/body/div[1]/div[5]/div/table/tbody/tr[2]/td[1]/a""")
    DISCOUT_IN_EMAIL_LABEL = (By.XPATH,
                              """/html/body/div[1]/div[4]/div/div/div[4]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/table[7]/tbody/tr/td/table[2]/tbody/tr/td/table[4]/tbody/tr/td[1]""")

    def __init__(self, driver):
        super().__init__(driver)

    def get_email(self) -> str:
        """ click button to copy new email and return this email """
        self.do_click(self.NEW_EMAIL_LABEL)
        email = pc.paste()
        return email

    def wait_for_email_to_confirm(self, max_wait: int) -> bool:
        """
        Function that wait for email
        :param max_wait: max waiting time [s]
        :return: True if email arrived, False if not
        """
        if max_wait < 60:
            raise Exception("Not enough time! Put a larger number of max_wait")

        current_waiting_time = 0
        while current_waiting_time < max_wait:
            titile_first_mail = self.get_element_text(self.FIRST_EMAIL)  # get title of newest mail
            if titile_first_mail == "Zalando Team <info@service-mail.zalando.pl>":  # if newest mail is from zalando
                return True
            else:
                current_waiting_time += 15
                time.sleep(15)
        return False

    def confirm_mail(self) -> None:
        """ Click a confirmation in first mail from zalando """
        self.do_click(self.FIRST_EMAIL)

        time.sleep(3)
        self.driver.refresh()  # close an add

        self.do_click(self.FIRST_EMAIL)  # again open newest mail
        if self.is_visible(self.CONFIRM_EMAIL_LABEL):
            self.do_click(self.CONFIRM_EMAIL_LABEL)

    def wait_for_email_with_discout(self, max_wait) -> bool:
        """
        Wait for email with discout code
        :param max_wait: max duration on waiting for email with code
        :return: True if email came
        """
        if max_wait < 60:
            raise Exception("Not enough time! Put a larger number of max_wait")

        current_waiting_time = 0
        while current_waiting_time < max_wait:
            try:
                email_with_code = self.get_element_text(self.EMAIL_WITH_CODE_VISIBLE)  # get title of newest mail
                if email_with_code == "Cieszymy się, że jesteś z nami":  # if newest mail is from zalando
                    return True
            except:
                current_waiting_time += 5
                time.sleep(5)
                self.driver.refresh()
        return False

    def get_discout_from_mail(self) -> str:
        """ click mail and get discout from it """
        self.do_click(self.EMAIL_WITH_CODE)
        if self.is_visible(self.DISCOUT_IN_EMAIL_LABEL):
            return self.get_element_text(self.DISCOUT_IN_EMAIL_LABEL)
