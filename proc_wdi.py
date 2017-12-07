#!/usr/bin/env python3

import csv
import sys
import re

from devec_sql_common import *

print_insert_header()


def units_heuristic(units):
    if units.startswith('%'):
        return "Unitless"
    if units.endswith('%'):
        return "Unitless"
    units = units.replace("international $", "international dollar")
    units = units.replace("US$", "US dollar")
    return units


def metric_heuristic(metric, units):
    """Use the separated metric and units names to come up with a new metric
    name."""
    if units.startswith('% of'):
        return metric + " (percent of" + units[len('% of'):] + ")"
    if units.startswith("% net"):
        return metric + " (percent net)"
    if units.startswith("% gross"):
        return metric + " (percent gross)"
    return metric


insert_line = "insert into data(region, odate, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

if __name__ == "__main__":
    with open("WDIData.csv", newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            s = re.search(r"\(([^()]+)\)$", row['Indicator Name'])
            units = ""
            metric = row['Indicator Name']
            if s:
                units = s.group(1)
                # strip off the units part of the metric, since units were found
                metric = metric_heuristic(metric[:-(len("(" + units +")"))].strip(), units)
                units = units_heuristic(units)
            for year in range(1960, 2017):
                y = str(year)
                if row[y]:
                    if first:
                        print(insert_line)
                    print("    " + ("" if first else ",") + "(" + uniq_join([
                        # The World Bank CSV starts with U+FEFF; rather than
                        # modifying the CSV (it is huge and would need to be done
                        # each time it is downloaded), we use the botched header
                        # name it gives
                        mysql_quote(region_normalized(row['\ufeff"Country Name"'])),  # region
                        mysql_string_date(y),  # odate
                        mysql_quote("https://web.archive.org/web/20171012171000/http://databank.worldbank.org/data/download/WDI_csv.zip"),  # database_url
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


print_insert_footer()
