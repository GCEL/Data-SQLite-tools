"""
A utility for quickly inspecting csv files

Python 2 version

DAV January 2018
"""

import csv

def show_csv_headers(csvfile):
  """Reads the header from a csv file and prints
     out the column headings.

     Args:
         csvfile: full path and name of the csv file

     Returns:
        A list of header column names
     """
  with open(csvfile) as f:
    reader = csv.reader(f)
    i = next(reader)
    print i



