from os import system
from pdf_to_data import extract
from site_to_links import get_epd_urls

#Links to the epddanmark, epd source
database_url = 'https://www.epddanmark.dk/epd-databasen/'
base_url = 'https://www.epddanmark.dk'

#TODO
#Add an option for camelot lattice with increased accuracy by installing ghostscript
#Add a flag -ghostscript that will use camelot lattice (and ghostscript) instead of  camelot stream
#stream and lattice a different ways camelot can get the tables from pdfs


def main():
    list_url = get_epd_urls(base_url, database_url)
    

    extract(list_url, 3)


if __name__ == "__main__":
    main()



