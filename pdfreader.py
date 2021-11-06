import tabula

file1 = "single_epd.pdf"
table = tabula.read_pdf(file1,pages=6, multiple_tables=True)
print(table[0])