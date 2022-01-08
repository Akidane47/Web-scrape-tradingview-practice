import requests
from bs4 import BeautifulSoup as bs 


##exchange_name = input('Input Github User: ') for searching stocks, still not responsive
#attempting simple scrape this time with span class identified
url = 'https://www.tradingview.com/'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
index_name = soup.find("span", attrs = {"class":"tv-widget-watch-list__description tv-widget-watch-list__description--uppercase apply-overflow-tooltip"})
for span in index_name:
    print(span.text)
print(url)



#class="tv-widget-watch-list__description tv-widget-watch-list__description--uppercase apply-overflow-tooltip"



#This code works due to span having a class unlike webscrape.py