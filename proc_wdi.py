#!/usr/bin/env python3

import csv
import sys
import re

from util import *


insert_line = "insert into data(region, year, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

with open("WDIData.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        s = re.search(r"\(([^()]+)\)$", row['Indicator Name'])
        units = ""
        metric = row['Indicator Name']
        if s:
            units = s.group(1)
            # strip off the units part of the metric, since units were found
            metric = metric[:-(len(" (" + units +")"))]
        for year in range(1960, 2017):
            y = str(year)
            if row[y]:
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    # The World Bank CSV starts with U+FEFF; rather than
                    # modifying the CSV (it is huge and would need to be done
                    # each time it is downloaded), we use the botched header
                    # name it gives
                    mysql_quote(row['\ufeff"Country Name"']),  # region
                    mysql_int(y),  # year
                    mysql_quote("https://data.worldbank.org/data-catalog/world-development-indicators"),  # database_url
                    mysql_quote(""),  # data_retrieval_method
                    mysql_quote(metric),  # metric
                    mysql_quote(units),  # units
                    mysql_float(row[y]),  # value
                    mysql_quote(""),  # notes
                ]) + ")")
                first = False
                count += 1
                if count > 5000:
                    count = 0
                    first = True
                    print(";")
    if not first:
        print(";")
