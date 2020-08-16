import csv, sqlite3

connection = sqlite3.connect(":memory:") # change to 'sqlite:///your_filename.db'
cur = connection.cursor()
cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

with open('data.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
connection.commit()
connection.close()



pip install csv-to-sqlite

import csv_to_sqlite 

# all the usual options are supported
options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 
input_files = ["abilities.csv", "moves.csv"] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "output.sqlite", options)