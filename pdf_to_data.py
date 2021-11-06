import requests

def download_epd_pdf(url):
    r = requests.get(url, allow_redirects=True)
    with open("./PDFs/single_epd.pdf", 'wb') as f:
        f.write(r.content)
