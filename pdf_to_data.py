import requests

def download_epd_pdf(url):
    r = requests.get(url, allow_redirects=True)
    with open("./PDFs/single_epd.pdf", 'wb') as f:
        f.write(r.content)

#Populates an EPD python object with data from the pdf
def populate_epd_object():
    