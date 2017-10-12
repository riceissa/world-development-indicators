#!/usr/bin/env python3

import csv
import sys
import re


with open("WDIData.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row['Indicator Name'])
