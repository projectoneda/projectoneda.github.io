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
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import shutil
from html.parser import HTMLParser

#------------------------------------------------------
# IMPORT STOCK DATA VARIABLES FROM SCRAPE.PY FILE
#------------------------------------------------------
from stock_scrape import stock_dict
#------------------------------------------------------

print(stock_dict)

stock_df = pd.DataFrame.from_dict(stock_dict)
stock_df.head()

#with open ('./Valuation_Guides/Valuation_Templates/Sample_Data.csv', newline='', encoding = 'utf-8') as csvfile:
#    reader = csv.reader(csvfile)
#    for row in reader:
#        print(row)

# 1/12/19 - Using sample/dummy data to begin calculations
# Will pull data once webscraping is complete
# Read csv file into pandas data frame
stocks_df = pd.read_csv('./Valuation_Guides/Valuation_Templates/Sample_Data.csv', 
                          index_col = 0)

# check - print to check dataframe was created correctly
print(stocks_df.head())

# print df column names
print(stocks_df.columns)

#------------------------------------------------
# P/E RATIO SUMMARY
#------------------------------------------------
# average P/E TTM
pe_mean = stocks_df['PE TTM'].mean()
print(pe_mean)

# median P/E TTM
pe_med = stocks_df['PE TTM'].median()
print(pe_med)


# Convert data to pandas dataframe




# pd.DataFrame.from_dict()

