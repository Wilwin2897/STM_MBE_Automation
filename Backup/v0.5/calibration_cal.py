# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:01:17 2022

@author: wilwin
"""

import numpy
import pandas as pd

# Load the xlsx file
def read_calibration_file(filename):
    xls = pd.ExcelFile('calibration_data.xlsx')
    df1 = pd.read_excel(xls, 'Te')
    df2 = pd.read_excel(xls, 'Sn')
    df3 = pd.read_excel(xls, 'BaF2')
    df4 = pd.read_excel(xls, 'Co')
    df5 = pd.read_excel(xls, 'Fe')
    df6 = pd.read_excel(xls, 'Dy')

print(df5)