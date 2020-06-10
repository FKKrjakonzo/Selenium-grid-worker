#!/usr/bin/python
# -*- coding: utf-8 -*-
import viktor2_functions as functions

from concurrent.futures import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import threading
import re

WEBPAGE = 'XXXXXX'

"""Edition of single user
Inputs - user URL, Data, Position ID in datafile.
"""
def single_user_edit(vybrany, data, pos):
    error = ''
    last = []
    last.append(data[-1] + '$')
    options = functions.options
    browser = webdriver.Firefox(options=options,
                                executable_path=r'C:\geckodriver\geckodriver.exe'
                                )
    browser.set_page_load_timeout(50)

    t = threading.Thread(target=functions.login(browser))
    t.start()

    while t.isAlive():
        pass

    try:
        url = WEBPAGE + vybrany[len(vybrany) - 1]
        browser.get(url)
        frame = browser.find_element_by_class_name('btn-edit')
        frame.click()

        values_single = [
            'User_FirstName',
            'User_LastName',
            'User_UserNameOtherSystem',
            'User_AddressCity',
            'User_AddressPostCode',
            'User_AddressStreet',
            'User_AddressStreetNumber',
            'User_Email',
            'User_PhoneNumber',
            'Allianz',
            'AXA poji\xc5\xa1\xc5\xa5ovna',
            '\xc4\x8cesk\xc3\xa1 Poji\xc5\xa1\xc5\xa5ovna',
            '\xc4\x8cPP',
            '\xc4\x8cSOB Poji\xc5\xa1tovna',
            'Direct Poji\xc5\xa1\xc5\xa5ovna',
            'Generali',
            'Kooperativa',
            'Slavia poji\xc5\xa1\xc5\xa5ovna',
            'UNIQA',
            ]

        values_choose = ['User_Valid', 'User_InsuringAllowed',
                         'User_SelectedRoleId']

        delay = 50  # seconds

        try:
            myElem = WebDriverWait(browser,
                                   delay).until(EC.presence_of_element_located((By.ID,
                    'User_FirstName')))
        except TimeoutException:
            return '.Failed to log in'

        page_data = re.sub('<[^<]+?>', '', browser.page_source)

        for u in range(len(values_single)):
            if len(str(data[u])) > 0:
                if u > 8:
                    frame = \
                        browser.find_element_by_id(page_data.split(values_single[u])[1].split('"'
                            )[0])
                else:
                    frame = browser.find_element_by_id(values_single[u])

                try:
                    last.append(frame.get_attribute('value') + '$')

                    frame.clear()
                    if str(data[u]) != 'nic':
                        if str(data[u])[-1] == ' ':
                            data[u] = str((data[u])[:-1])
                        frame.send_keys(str(data[u]))
                except:
                    if '.Fail_0_in_' not in error:
                        error += '.Fail_0_in_' + str(pos)
            else:
                last.append(' ' + '$')

        for u in range(len(values_choose)):
            frame = browser.find_element_by_id(values_choose[u])

            if len(str(data[len(values_single) + u])) > 0:
                try:
                    Select(frame).select_by_value(str(data[len(values_single)
                            + u]))
                except Exception, e:
                    print e
                    if '.Fail_1_in_' not in error:
                        error += '.Fail_1_in_' + str(pos)

        frame = browser.find_element_by_class_name('btn-blue')
        frame.click()
    except Exception, e:

        print e
        browser.quit()
        return '---FAIL ' + str(data[-1]) + ','
    error += '---SUCCESS' + str(data[-1]) + ','
    browser.quit()
    last.append(error)
    print error
    return last
