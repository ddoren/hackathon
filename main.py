from pdf_to_data import extract_data_from_url
from site_to_links import get_epd_urls

#Links to the epddanmark, epd source
database_url = 'https://www.epddanmark.dk/epd-databasen/'
base_url = 'https://www.epddanmark.dk'

#TODO
#Add an option for camelot lattice with increased accuracy by installing ghostscript
#Add a flag -ghostscript that will use camelot lattice (and ghostscript) instead of  camelot stream
#stream and lattice a different ways camelot can get the tables from pdfs


def main():
    url_list = get_epd_urls(base_url, database_url)

    extract_data_from_url(url_list)


if __name__ == "__main__":
    main()


#WE THE MFcks who push directly into main \_/
