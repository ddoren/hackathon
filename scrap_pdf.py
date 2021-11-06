import ctypes
from ctypes.util import find_library
find_library("".join(("gsdll", str(ctypes.sizeof(ctypes.c_voidp) * 8), ".dll")))
import camelot 

file = 'single_epd.pdf'
pdf = camelot.read_pdf(file)
print("Total tables extracted:", pdf)