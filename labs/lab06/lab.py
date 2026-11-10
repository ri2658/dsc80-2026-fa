# lab.py


import os
import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.21')
import requests
import bs4
import lxml


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def question1():
    """
    NOTE: You do NOT need to do anything with this function.
    The function for this question makes sure you
    have a correctly named HTML file in the right
    place. Note: This does NOT check if the supplementary files
    needed for your page are there!
    """
    # Don't change this function body!
    # No Python required; create the HTML file.
    return


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def extract_book_links(text):
    soup = bs4.BeautifulSoup(text, features='lxml')

    links = []

    for book in soup.find_all('article', class_='product_pod'):
        href = book.find('h3').find('a')['href']
        rating = book.find('p', class_='star-rating')['class'][1]
        price = book.find('p', class_='price_color').text.strip('Â£')

        if rating in {'Four', 'Five'} and float(price) < 50.00:
            links.append(href)

    return links

def get_product_info(text, categories):
    soup = bs4.BeautifulSoup(text, features='lxml')

    category = soup.find('ul', class_='breadcrumb').find_all('a')[-1].text
    info = {}


    if category in categories:
        info['Category'] = category
        info['Rating'] = soup.find('p', class_='star-rating')['class'][1]
        info['Title'] = soup.find('h1').text
        info['Description'] = soup.find('div', id='product_description').find_next_sibling('p').text

        table = soup.find('table', class_='table-striped')

        for tr in table.find_all('tr'):
            info[tr.find('th').text] = tr.find('td').text
            
        return info

    return None

def scrape_books(k, categories):
    rows = []
    
    for i in range(1, k+1):
        page = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html')
        extract_book_out = extract_book_links(page.text)

        for url in extract_book_out:
            text = requests.get(f'http://books.toscrape.com/catalogue/{url}').text
            info = get_product_info(text, categories)
            if info is not None:
                rows.append(info)
        df = pd.DataFrame(rows)

    return df


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def stock_history(symbol, year, month):
    start_date = pd.Timestamp(year=year, month=month, day=1)
    dates = pd.date_range(start=start_date, periods = start_date.days_in_month, freq='D')
    
    params = {
        'symbol': symbol,
        'from': f'{year}-{month:02d}-01',
        'to':   f'{year}-{month:02d}-{start_date.days_in_month:02d}',
        'apikey': 'czHUKml5OxAG78Fwv8ky3RMaX0LCqJ2x'
    }

    data = requests.get('https://financialmodelingprep.com/stable/historical-price-eod/full', params=params).json()
    df = pd.DataFrame(data)

    return df

def stock_stats(history):
    price_change = (history.iloc[0]['close'] - history.iloc[-1]['open'])/history.iloc[-1]['open'] * 100
    dtv = ((history.loc[:, 'high'] + history.loc[:, 'low'])/2 * history.loc[:, 'volume']).sum()


    return (
        f'{price_change:+.2f}%',
        f'{dtv/1e9:.2f}B'
    )


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def get_comments(storyid):
    ...
