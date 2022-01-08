import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#first attempt to scrape and print all table data


stock_ticker = input("Enter NASDAQ ticker: ")
url = "https://tradingview.com/symbols/NASDAQ-"+stock_ticker
r = requests.get(url)
soup = bs(r.text, "html.parser")
stock_price = soup.find("div", class_ = "tv-symbol-price-quote__value js-symbol-last")
for div in stock_price:
    print(div.text)


