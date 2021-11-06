import requests
from bs4 import BeautifulSoup

def download_epd_pdf(url):
    r = requests.get(url, allow_redirects=True)
    with open("single_epd.pdf", 'wb') as f:
        f.write(r.content)

database_url = 'https://www.epddanmark.dk/epd-databasen/'


base_url = 'https://www.epddanmark.dk'

def get_epd_urls():
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
    return url_list

download_epd_pdf(get_epd_urls()[2])

print (get_epd_urls())




def main():
    #Creates a list with download links for each epd available on the site
    url_list = get_epd_urls(base_url, database_url)

    #Downloads the pdfs and extracts the necessary data from them, for each epd as a python object and returns a list of those objects
    extract_data_from_url(url_list)




if __name__ == "__main__":
    main()



