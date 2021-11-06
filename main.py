from site_to_links import get_epd_urls

#Links to the epddanmark, epd source
database_url = 'https://www.epddanmark.dk/epd-databasen/'
base_url = 'https://www.epddanmark.dk'


def main():
    url_list = get_epd_urls(base_url, database_url)

    extract_data_from_url(url_list)


if __name__ == "__main__":
    main()



