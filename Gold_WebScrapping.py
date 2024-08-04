import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    # Find all divs with the specified class
    web_content_div = web_content.find_all('div', {'class': class_path})
    texts = []  # Initialize texts to return

    if web_content_div:  # Check if any divs were found
        try:
            spans = web_content_div[0].find_all('span')
            texts = [span.get_text() for span in spans]
        except IndexError:
            print("Error: No spans found in the div.")
    
    return texts

def real_time_price(stock_code):
    url = 'https://finance.yahoo.com/quote/%5EGSPC'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        # Ensure to check the right class name in the Yahoo Finance page
        texts = web_content_div(web_content, 'container yf-aay0dk')  
        
        # Check if any text was retrieved
        if texts:
            price, change = texts[0], texts[1]
        else:
            print("Error: Texts list is empty.")
            price, change = None, None
    except ConnectionError:
        print("Error: Connection error occurred.")
        price, change = None, None
    
    return price, change

stock = ['S&P 500']
print(real_time_price('S&P 500'))
