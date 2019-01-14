from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import shutil
import re

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

# Create empty dictionary to hold data - stock tickers will be used as keys
stock_dict = {}

# Create list which contains headings for financial data to be scraped
fin_data = ['Name',
            'Price',
            'Day Range',
            '52W_Range',
            'Volume',
            'Average Volume',
            'Market Cap',
            'PE Ratio',
            'Dividend Yield',
            'Beta']

#----------------------------------------------------------------------
# Goldman Sachs
#----------------------------------------------------------------------
url = "https://www.marketbeat.com/stocks/NYSE/GS/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
gs_title = soup.find("h1", class_="PageTitleHOne").text
gs  = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')
print(gs_title)

#------------------------------------------------------------------------------------
# THE STEPS BELOW WILL BE REPEATED FOR ALL STOCKS (PRINT STATEMENTS WILL BE REMOVED)
# WE CAN RE-VISIT LATER ON AND CREATE FOR LOOP TO SCRAPE AND CLEAN ALL DATA
#------------------------------------------------------------------------------------
# Loop through LIST produced in Beautiful Soup "find_all" function above and strip html tags (<strong>)

# Empty list to hold financial data with stripped tags
gs_nt =[]

for data in gs:
    
    # Pull list elements 1 by 1 and put into string
    data_str = str(data)
    print(data_str)
    
    # Put element string into beautiful soup object
    b_soup = bs(data_str)
    print(b_soup)
    
    # Strip html tag from list elements
    data_text = b_soup.get_text()
    print(data_text)
    
    # Add data to list
    gs_nt.append(data_text)
    print(gs_nt)

# Pull company name from title string,strip blank spaces and append beggining of fin data list
gs_name = re.split(r'\bStock\b|:|- ',gs_title)[2]
gs_nt.insert(0,gs_name.strip())
print(gs_name)

# Zip fin_data list with stock data
gs_zip = list(zip(fin_data,gs_nt))
print(gs_zip)

print(gs_title)
print(gs)
print(gs_nt)

# Pull stock ticker from title string and strip blank spaces
tick = (gs_title.split(':')[1])[0:3]
tick.strip()
print(tick)

# Add stock data to stock_dict with ticker as key and data as value
stock_dict[tick] = gs_zip
print(stock_dict)

#----------------------------------------------------------------------
# JP Morgan Chase
#----------------------------------------------------------------------
url = "https://www.marketbeat.com/stocks/NYSE/JPM/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
jp_title = soup.find("h1", class_="PageTitleHOne").text
jp  = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

# Empty list to hold financial data with stripped tags
jp_nt =[]

for data in jp:
    
    # Pull list elements 1 by 1 and put into string
    data_str = str(data)
    
    # Put element string into beautiful soup object
    b_soup = bs(data_str)
    
    # Strip html tag from list elements
    data_text = b_soup.get_text()
    
    # Add data to list
    jp_nt.append(data_text)

# Pull company name from title string,strip blank spaces and append beggining of fin data list    
jp_name = re.split(r'\bStock\b|:|- ',jp_title)[2]
print(jp_name)

jp_nt.insert(0,jp_name.strip())
print(jp_nt)

# Zip fin_data list with stock data
jp_zip = list(zip(fin_data,jp_nt))

# Pull stock ticker from title string and strip blank spaces
tick = (jp_title.split(':')[1])[0:3]
tick.strip()

# Add stock data to stock_dict with ticker as key and data as value
stock_dict[tick] = jp_zip
print(stock_dict)

#----------------------------------------------------------------------
# Bank of America
#----------------------------------------------------------------------

url = "https://www.marketbeat.com/stocks/NYSE/BAC/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
bac_title = soup.find("h1", class_="PageTitleHOne").text
bac = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

# Empty list to hold financial data with stripped tags
bac_nt =[]

for data in bac:
    
    # Pull list elements 1 by 1 and put into string
    data_str = str(data)
    
    # Put element string into beautiful soup object
    b_soup = bs(data_str)
    
    # Strip html tag from list elements
    data_text = b_soup.get_text()
    
    # Add data to list
    bac_nt.append(data_text)

# Pull company name from title string,strip blank spaces and append beggining of fin data list    
bac_name = re.split(r'\bStock\b|:|- ',bac_title)[2]
bac_nt.insert(0,bac_name.strip())

# Zip fin_data list with stock data
bac_zip = list(zip(fin_data,bac_nt))

# Pull stock ticker from title string and strip blank spaces
tick = (bac_title.split(':')[1])[0:3]
tick.strip()

# Add stock data to stock_dict with ticker as key and data as value
stock_dict[tick] = bac_zip
print(stock_dict)

#----------------------------------------------------------------------
# UBS
#----------------------------------------------------------------------
url = "https://www.marketbeat.com/stocks/NYSE/UBS/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
ubs_title = soup.find("h1", class_="PageTitleHOne").text
ubs = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(ubs_title)
print(ubs)

# Empty list to hold financial data with stripped tags
ubs_nt =[]

for data in ubs:
    
    # Pull list elements 1 by 1 and put into string
    data_str = str(data)
    
    # Put element string into beautiful soup object
    b_soup = bs(data_str)
    
    # Strip html tag from list elements
    data_text = b_soup.get_text()
    
    # Add data to list
    ubs_nt.append(data_text)

# Pull company name from title string,strip blank spaces and append beggining of fin data list    
ubs_name = re.split(r'\bStock\b|:|- ',ubs_title)[2]
ubs_nt.insert(0,ubs_name.strip())

# Zip fin_data list with stock data
ubs_zip = list(zip(fin_data,ubs_nt))

# Pull stock ticker from title string and strip blank spaces
tick = (ubs_title.split(':')[1])[0:3]
tick.strip()

# Add stock data to stock_dict with ticker as key and data as value
stock_dict[tick] = ubs_zip
print(stock_dict)

#----------------------------------------------------------------------
# Wells Fargo
#----------------------------------------------------------------------
url = "https://www.marketbeat.com/stocks/NYSE/WFC/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
wf_title = soup.find("h1", class_="PageTitleHOne").text
wf = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(wf_title)
print(wf)

# Empty list to hold financial data with stripped tags
wf_nt =[]

for data in wf:
    
    # Pull list elements 1 by 1 and put into string
    data_str = str(data)
    
    # Put element string into beautiful soup object
    b_soup = bs(data_str)
    
    # Strip html tag from list elements
    data_text = b_soup.get_text()
    
    # Add data to list
    wf_nt.append(data_text)
    
# Pull company name from title string,strip blank spaces and append beggining of fin data list    
wf_name = re.split(r'\bStock\b|:|- ',wf_title)[2]
wf_nt.insert(0,wf_name.strip())

# Zip fin_data list with stock data
wf_zip = list(zip(fin_data,wf_nt))

# Pull stock ticker from title string and strip blank spaces
tick = (wf_title.split(':')[1])[0:3]
tick.strip()

# Add stock data to stock_dict with ticker as key and data as value
stock_dict[tick] = wf_zip
print(stock_dict)

