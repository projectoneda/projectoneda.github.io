from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import shutil

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

# Goldman Sachs

url = "https://www.marketbeat.com/stocks/NYSE/GS/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
gs_title = soup.find("h1", class_="PageTitleHOne").text
gs  = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(gs_title)
print(gs)


# JP Morgan Chase

url = "https://www.marketbeat.com/stocks/NYSE/JPM/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
jp_title = soup.find("h1", class_="PageTitleHOne").text
jp  = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(jp_title)
print(jp)


# Bank of America

url = "https://www.marketbeat.com/stocks/NYSE/BAC/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
bac_title = soup.find("h1", class_="PageTitleHOne").text
bac = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(bac_title)
print(bac)


# UBS

url = "https://www.marketbeat.com/stocks/NYSE/UBS/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
ubs_title = soup.find("h1", class_="PageTitleHOne").text
ubs = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(ubs_title)
print(ubs)


# Wells Fargo

url = "https://www.marketbeat.com/stocks/NYSE/WFC/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
wf_title = soup.find("h1", class_="PageTitleHOne").text
wf = soup.find("div", class_="col-md-9 price-data-section").find_all('strong')

print(wf_title)
print(wf)
