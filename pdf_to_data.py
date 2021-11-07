import requests
import camelot
import os
import json

epd_pop_list = []
temp_pdf_location = "./temp_pdf/single_epd.pdf"

#Downloads the pdf and puts it in the temp_pdf directory
def download_epd_pdf(url):
    r = requests.get(url, allow_redirects=True)
    with open(temp_pdf_location, 'wb') as f:
        f.write(r.content)

#Extracts all the tables from one epd link as json and puts them in temp_json folder
def get_json_tables():
    tables = camelot.read_pdf(temp_pdf_location, flavor='stream', pages='all')
    print(f'Found {tables.__len__()} tables at {temp_pdf_location}')
    tables.export('temp_json/table.json', f='json')

#Goes through all the created files and finds the exact needed table 
def find_exact_table(tableList):
    for table in tableList:
        jsonFile = json.load(open(table))
        
        if 'ENVIRONMENTAL IMPACTS PER KG' in str(jsonFile) or 'RESOURCE USE PER DECLARED UNIT' in str(jsonFile):
            print(f'! Found the table at {table} !')
            #TODO, get the exact table location by splitting the table after page - <> and table - <> 
            #will greatly improve accuracy
            #table_location = table.split("world",1)
            return table

#Removes all the contents of the temp_json folder, !use only after the python object has been created!
def flush_temp_json():
    filelist = [ f for f in os.listdir('./temp_json') if f.endswith(".json") ]
    for f in filelist:
        os.remove(os.path.join('./temp_json', f))

#populates a python object from a json file
def populate_epd_object_from_json(table):
    whole_table = json.load(open(table))
    print(whole_table[1])
    print(whole_table[2])
    print(f'Entries Found {len(whole_table[2])}')
    first_row = whole_table[1]
    print(whole_table[1])
    #TODO


def extract(url_list):
    print(f'Found {len(url_list)} EPDs Starting the extraction')
    limit = 1
    iteration = 0
    for url in url_list:

        download_epd_pdf(url)

        all_tables = get_json_tables()

        needed_table = find_exact_table(all_tables)

        iteration += 1
        if iteration > limit:
            break

        
# get_json_tables(temp_pdf_location)
flush_temp_json()

# populate_epd_object_from_json('./temp_json/table-page-8-table-1.json')
# find_exact_table(get_all_tables())
    