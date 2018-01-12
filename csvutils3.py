"""

Utils for inspecting csv files

DAV

Python 3 version
"""

import csv

def show_csv_headers(csvfile):
  """Prints a list of all the headers in a csv file"""
  with open(csvfile, "rb") as f:
      reader = csv.reader(f)
      i = next(reader)

      print(i)

