#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import wget
import zipfile
import os
from os import listdir
from os.path import isfile, join
import shutil

WEBSITE = 'XXXXXXXXX'

"""Download ZIP with updated files
"""
def download():
    col_dict = {
        'a': str,
        'b': str,
        'c': str,
        'd': str,
        'e': str,
        'f': str,
        'g': str,
        'h': str,
        'i': str,
        'j': str,
        'k': str,
        'l': str,
        ',m': str,
        'n': str,
        'o': str,
        'p': str,
        'q': str,
        'r': str,
        's': str,
        't': str,
        'u': str,
        'v': str,
        'w': str,
        }
    try:
        os.remove('VIKTOR_Carkulka.zip')
        shutil.rmtree('VIKTOR_Carkulka')
    except:
        pass

    try:
        wget.download(WEBSITE)
    except:
        return '$Failed downloading'
    with zipfile.ZipFile('VIKTOR_Carkulka.zip', 'r') as zip_ref:
        zip_ref.extractall()

    fileDir = os.path.dirname(os.path.realpath('__file__'))

    mypath = os.path.join(fileDir,
                          'VIKTOR_Carkulka/UPRAVA_UZIVATELOV.xlsx')

    xlsx = pd.read_excel(mypath, sheet_name=0, dtype=str,
                         na_filter=False)

    sheet1 = xlsx
    sheet1.fillna('', inplace=True)

    sheet1 = sheet1.values.tolist()

    return sheet1
