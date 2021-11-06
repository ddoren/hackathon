from bs4 import BeautifulSoup
import requests
import ctypes
from ctypes.util import find_library


database_url = 'https://www.epddanmark.dk/epd-databasen/'


base_url = 'https://www.epddanmark.dk'


url_list = []


page = requests.get(database_url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll('div', {'class': 'small-12 medium-12 large-12 columns'})
for r in results:
    a_list = r.findAll('a')
    if len(a_list) > 0:
        href = a_list[1]['href']
        if not href.startswith('/media'):
            continue
        url_list.append(base_url + href)

