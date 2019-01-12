#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 00:09:48 2019

@author: donaldwalker
"""
import os
import csv
import numpy as np
import pandas as pd

#with open ('./Valuation_Guides/Valuation_Templates/Sample_Data.csv', newline='', encoding = 'utf-8') as csvfile:
#    reader = csv.reader(csvfile)
#    for row in reader:
#        print(row)

stocks_df = pd.read_csv('./Valuation_Guides/Valuation_Templates/Sample_Data.csv', index_col = 'Company')

stocks_df.head(2)


# 1/12/19 - Using sample/dummy data to begin calculations
# Will pull data once webscraping is complete



# Convert data to pandas dataframe




# pd.DataFrame.from_dict()

