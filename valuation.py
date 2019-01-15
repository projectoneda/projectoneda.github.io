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
from pandas.io.json import json_normalize

#------------------------------------------------------
# IMPORT STOCK DATA VARIABLES FROM SCRAPE.PY FILE
#------------------------------------------------------
from stock_scrape import stock_dict,fin_data
#------------------------------------------------------

# Create dataframe to hold company data
stock_df = pd.DataFrame.from_dict(stock_dict, 
                                  orient = 'index', 
                                  columns = fin_data)
stock_df.head(20)


#------------------------------------------------
# APPEND RANDOM EPS ESTIMATES TO DF FOR EACH STOCK
#------------------------------------------------

# Place stock tickers into list
tickers = list(stock_dict.keys())
print(tickers)

rand = np.random.uniform(5,20)
print(rand) 

# Empty lists to hold EPS and PE variables
earns = []
p_to_e= []

# loop to generate random EPS and PE ratios
for ticks in tickers:
    
#   Generate random EPS and PE estimates
    EPS_rand =  np.random.uniform(5,20)
    PE_rand = np.random.uniform(5,20)
    
#   Append EPS and PE to earns and p_to_e lists
    earns.append(round(EPS_rand,2))
    p_to_e.append(round(PE_rand,2))
     
# Zip eps, pe and tickers lists
EPS_ticks = list(zip(tickers,earns,p_to_e))
    
print(EPS_ticks)

# Place estimates into dataframe   
estimates_df = pd.DataFrame(EPS_ticks,columns=['Ticker','EPS','PE'])        
    
# Merge estimates_df and stock_df

stock_df = stock_df.reset_index()
stock_df = stock_df.rename(columns={'index':'Ticker'})
stock_df.head()

stock_data_df = stock_df.merge(estimates_df,on='Ticker')
stock_data_df.head()

# Insert price target column (EPS (estimated) * PE (estimated))
stock_data_df['Target'] = stock_data_df.EPS * stock_data_df.PE
stock_data_df.head()

# Define function to convert currency string in df to float
# ----Copied from http://pbpython.com/pandas_dtypes.html----

def convert_currency(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)  

# Convert Price column to currency
stock_data_df['Price'] = stock_data_df['Price'].apply(convert_currency)
stock_data_df.dtypes

# Insert Reccomendation column which will state...
# Buy, Sell, or hold if PE x EPS is less than, greater than, or equal to current price
stock_data_df.loc[
                  stock_data_df.Price < stock_data_df.Target,
                  'Reccomendation'] = 'BUY'

stock_data_df.loc[
                  stock_data_df.Price > stock_data_df.Target,
                  'Reccomendation'] = 'SELL'

stock_data_df.head()

# ------------------------------------------------------------------------------
# PLACE STOCK DATA INTO VARIABLES TO LOAD INTO STOCKS.HTML (VIA APP.PY)     
# ------------------------------------------------------------------------------
fin_dict = stock_data_df.to_dict()
print(fin_dict)

print(fin_dict['Ticker'].values())

for key, value in fin_dict['Ticker'].items():
    print(value)
    
for tick in stock_data_df['Ticker']:
    print(tick)

print(stock_data_df['Ticker'][0])   
    
    
    