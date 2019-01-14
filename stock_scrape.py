from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import shutil
import re

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

# Create empty dictionary to hold data - stock tickers will be used as keys
tickers = []
stock_dict = {}

#----------------------------------------------------------------------
# Goldman Sachs
#----------------------------------------------------------------------
url = "https://www.marketbeat.com/stocks/NYSE/GS/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
gs_title = soup.find("h1", class_="PageTitleHOne").text
gs  = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

# Strip html tag (<strong>) from list produced in "find_all" function above

# Empty list to hold new array with stripped tags
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

print(gs_title)
print(gs)
print(gs_nt)

# Pull stock ticker from title string
tick = (gs_title.split(':')[1])[0:3]

# Strip blank spaces from ticker and append ticker to "tickers" list
tickers.append(tick.strip())
print(tickers)

# Add ticker as key and data as value to dictionary
stock_dict[tick] = gs_nt
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

print(jp_title)
print(jp)

tick = (jp_title.split(':')[1])[0:3]
tickers.append(tick.strip())
print(tickers)

# Bank of America

url = "https://www.marketbeat.com/stocks/NYSE/BAC/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
bac_title = soup.find("h1", class_="PageTitleHOne").text
bac = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(bac_title)
print(bac)

tick = (bac_title.split(':')[1])[0:3]
tickers.append(tick.strip())
print(tickers)

# UBS

url = "https://www.marketbeat.com/stocks/NYSE/UBS/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
ubs_title = soup.find("h1", class_="PageTitleHOne").text
ubs = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(ubs_title)
print(ubs)

tick = (ubs_title.split(':')[1])[0:3]
tickers.append(tick.strip())
print(tickers)

# Wells Fargo

url = "https://www.marketbeat.com/stocks/NYSE/WFC/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
wf_title = soup.find("h1", class_="PageTitleHOne").text
wf = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(wf_title)
print(wf)

tick = (wf_title.split(':')[1])[0:3]
tickers.append(tick.strip())
print(tickers)



