import requests
from bs4 import BeautifulSoup

epd_links_list = []

def populate_link_list():
    #TODO automate this shit
    individual_link = 'https://www.epddanmark.dk/media/e2rbzqnl/md-20010-en_adfil.pdf'
    epd_links_list.append(individual_link)
    return epd_links_list

# def download_epd_pdf(url):
#     r = requests.get(url, allow_redirects=True)
#     with open("single_epd.pdf", 'wb') as f:
#         f.write(r.content)

# epd_links_list = populate_link_list()
# download_epd_pdf(epd_links_list[0])

link = 'https://www.epddanmark.dk/epd-databasen/'

page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
results1 = soup.findAll("div", {"class": "small-12 medium-12 large-12 columns"})

for r in results1:
    a = r.findAll('a')
    print(a)








