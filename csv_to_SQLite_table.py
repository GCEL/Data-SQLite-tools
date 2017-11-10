# -*- coding: utf-8 -*-
"""
This utility reads csv files and appends them to a SQLlite database as 
a new table or appends to an existing table.

Note: Only needed if using an older version of sqlite3 as newer versions
can do this for you with the SQLite .import command.

Author: DAV
Date: 10/11/17
"""
import sqlite3
import pandas

#database_name = os.environ.get('OxfordGEM.db')
database_name = "OxfordGEM.db"
datadir = "/home/dvalters/Datasets/Oxford_GEM/"

conn = sqlite3.connect(datadir + '/' + database_name)
cur = conn.cursor()

csvfile = 'stem_resp_raw.csv'
table_name = 'stem_resp_raw'

df = pandas.read_csv(datadir + csvfile, encoding='latin-1')

# Encoding issues in one of the csv files
#df = pandas.read_csv(datadir + csvfile, encoding='latin-1')
df.to_sql(table_name, conn, if_exists='append', index=False)
