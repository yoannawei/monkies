# convert a CSV file to a Dictionary

import os
import csv
import string

DATADIR = ""
datafile = "beatles-diskography.csv"

def parse_file(datafile):

    data = {}
    records = []
    with open(datafile) as file:
        # reads the first line of the csv datafile
        # forms a keys list composed of the column names
        keys = file.readline().rstrip().split(',')

        csv_file = csv.reader(file)

        # for each row in the csv csv_file
        # constructs a dictionary with keys from the keys list
        # and the items in the row as the values
        for row in csv_file:
            data = {k:v for k,v in zip(keys, row)}
            records.append(data)
            
    return records[0:10]

print(parse_file(datafile))
