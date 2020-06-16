#!/usr/bin/python
# -*- coding: utf-8 -*-
import viktor2_functions as functions
import viktor2_worker as worker
import viktor2_download as download
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from concurrent.futures import ThreadPoolExecutor
import csv
import sys
import os
from multiprocessing.pool import ThreadPool
import threading
import datetime

"""Main function
"""
def main():
    
    URL_SITE = 'XXXX'   
    exceli = download.download()
    options = functions.options
    browser = webdriver.Firefox(options=options,
                                executable_path=r'C:\geckodriver\geckodriver.exe'
                                )
    browser.set_page_load_timeout(50)
    functions.login(browser)
    browser.get(URL_SITE)
    page = re.sub('<[^<]+?>', '', browser.page_source)

    all_functional = []
    correct = []

    for i in page:
        all_functional.append(i.split('*'))
    del all_functional[:1]

    collected_data = []
 
    for i in range(len(exceli)):
        for u in range(len(all_functional)):
            if exceli[i][len(exceli[i]) - 1].lower() \
                in all_functional[u][5].lower():
                m = []
                for l in range(len(exceli[i]) - 1):
                    m.append(exceli[i][l])
                m.append(all_functional[u][0].replace(' ', ''))
                correct.append(m)
                collected_data.append(exceli[i])
   
    browser.quit()

    futures = []
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    mypath = os.path.join(fileDir, 'log.txt')
    f = open(mypath, 'a+')
    
    collected_data = ["Test", "Test", "Test", "Test"]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for link in range(len(correct)):
            futures.append(ex.submit(worker.single_user_edit,
                           correct[link], collected_data[link], link))

    print(futures)

 
if __name__ == '__main__':
    main()
