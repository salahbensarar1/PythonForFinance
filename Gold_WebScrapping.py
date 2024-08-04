import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
 
def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class' : class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [spans.get_text() for span in spans]
    except IndexError:
        texts = []
        return texts
  
def ream_time_price(stock_code):
     url = 'https://finance.yahoo.com/quote/%5EGSPC'
     try:
         r = requests.get(url)
         web_content = BeautifulSoup(r.text, 'lxml')
         texts = web_content_div(web_content,'container yf-aay0dk')
         if texts != []:
             price, change = texts[0], texts[1]
         else:
             price, change = [],[]
     except ConnectionError:
         price, change = [], []
     return  price, change
 
Stock = ['S&P 500']
print(ream_time_price('S&P 500'))