#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import xlrd
import statistics as st
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    thesheet = workbook.sheet_by_index(0)

    sheet_data = [[thesheet.cell_value(r, col)
                for col in range(thesheet.ncols)]
                for r in range(thesheet.nrows)]

    num_rows = thesheet.nrows
    num_cols = thesheet.ncols

    # Get the min, max and avg of values in column 1

    coast = thesheet.col_values(1, start_rowx=1, end_rowx=num_rows)

    min_val, min_index = min((coast[i], i) for i in range(len(coast)))

    min_time = thesheet.cell_value(min_index, 0)

    max_val, max_index = max((coast[i], i) for i in range(len(coast)))

    max_time = thesheet.cell_value(max_index, 0)

    avg_val = st.mean(coast)

    maxtime = xlrd.xldate_as_tuple(max_time, 0)
    mintime = xlrd.xldate_as_tuple(max_time, 0)

    data = {
            'maxtime': maxtime,
            'maxvalue': max_val,
            'mintime': mintime,
            'minvalue': min_val,
            'avgcoast': avg_val
    }
    return data


def test():
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 16, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)

    print("test passed")
test()
