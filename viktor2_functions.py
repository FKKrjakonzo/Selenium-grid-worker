#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

options = Options()
PAGE_URL = 'XXXXX'
USERNAME = 'XXXXX'
PASSWORD = 'XXXXX'

options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--blink-settings=imagesEnabled=false')

"""Login function, input selenium browser object
"""
def login(browser):
    browser.set_page_load_timeout(50)

    browser.get(PAGE_URL)
    delay = 50  # seconds
    try:
        myElem = WebDriverWait(browser,
                               delay).until(EC.presence_of_element_located((By.ID,
                'UserName')))
    except TimeoutException:
        return '.Failed to log in'
    frame = browser.find_element_by_id('UserName')
    frame.send_keys(USERNAME)
    frame = browser.find_element_by_id('Password')
    frame.send_keys(PASSWORD)
    frame = browser.find_element_by_class_name('btn-orange')
    frame.click()
