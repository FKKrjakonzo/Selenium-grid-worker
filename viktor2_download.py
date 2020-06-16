#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO;
WEBSITE = 'XXXXX'

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
    resp = urlopen(WEBSITE)
    zipfile = ZipFile(BytesIO(resp.read()))
    obj = zipfile.open('VIKTOR_Carkulka/UPRAVA_UZIVATELOV.xlsx')
    xlsx = pd.read_excel(obj, sheet_name=0, dtype=str,
                         na_filter=False)
    xlsx.fillna('', inplace=True)
    return xlsx.values.tolist()
