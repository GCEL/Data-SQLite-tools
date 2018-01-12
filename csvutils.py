"""
A utility for quickly inspecting csv files

Python 2 version

DAV January 2018
"""

import csv
import unittest
import pickle

def show_csv_headers(csvfile):
  """Reads the header from a csv file and prints
     out the column headings.

     Args:
         csvfile: full path and name of the csv file

     Returns:
        A list of header column names
     """
  listy = []
  with open(csvfile) as f:
    reader = csv.reader(f)
    i = next(reader)
    print i
    listy.append(i)
  return listy

class TestCsvReaders(unittest.TestCase):

  def test_readsimplecsvheader(self):
    
    csv_mock = [('foo', 'bar', 'baz')] 
    with open("test.csv", 'wb') as csvtest:
      wr = csv.writer(csvtest, dialect='excel')
      wr.writerows(csv_mock)

    self.assertEqual(show_csv_headers("test.csv"), [['foo', 'bar', 'baz']])

if __name__=='__main__':
  unittest.main()

    

