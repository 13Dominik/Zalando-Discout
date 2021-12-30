#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.EmailPage import EmailPage
from pages.ZalandoPage import ZalandoPage


def get_discout() -> str:
    """ do all steps to get discout"""
    # initialize driver and pages
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    ep = EmailPage(driver)
    zp = ZalandoPage(driver)

    ep.driver.get(ep.PAGE_URL)  # open email page
    new_mail = ep.get_email()  # get new email
    print(f"new email taken: {new_mail}")

    driver.execute_script("window.open('');")  # open second page
    driver.switch_to.window(driver.window_handles[1])
    zp.driver.get(zp.PAGE_URL)

    zp.pass_email(new_mail)  # do all on zalando page
    zp.click_fashion()
    zp.click_save()
    print("Zalando operations done!")

    driver.switch_to.window(driver.window_handles[0])  # back to email page
    print("Waiting for email to confirm...")
    if ep.wait_for_email_to_confirm(300):  # confirm mail
        ep.confirm_mail()
        print("Email confirmed!")
    driver.switch_to.window(driver.window_handles[0])

    print("Waiting for email with code...")
    if ep.wait_for_email_with_discout(300):  # open email and get discout from email
        discout = ep.get_discout_from_mail()
        print(f"New discout: {discout}")
        return discout


def main():
    discout_code = get_discout()
    with open('discouts.txt', mode='a') as file_to_save:  # save discout to txt file
        file_to_save.write(f"{discout_code}\n")


if __name__ == '__main__':
    main()
