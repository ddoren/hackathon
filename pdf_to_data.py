import requests

epd_pop_list = []
temp_pdf_location = "./PDFs/single_epd.pdf"

def download_epd_pdf(url):
    r = requests.get(url, allow_redirects=True)
    with open(temp_pdf_location, 'wb') as f:
        f.write(r.content)

#Returns populated python epd object
def scrap_epd_pdf(temp_pdf_location):

    return

def extract_data_from_url(url_list):
    print(f'Found {len(url_list)} EPDs Starting the extraction')
    n = 0
    for url in url_list:
        print(f'EPD {n} our of {len(url_list)}, link: {url}')
        download_epd_pdf(url)
        #Scraps a pdf and puts in in a temporary epd object
        temp_epd = scrap_epd_pdf(temp_pdf_location)
        #Adds the epd object to the populated epd object list
        epd_pop_list.append(temp_epd)

    return epd_pop_list
    