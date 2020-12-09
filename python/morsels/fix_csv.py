#!/usr/bin/env python3
# fix_csv.py
""" This is my solution to fix_csv Morsel """

import csv

dialect = csv.register_dialect('comma_escaped', escapechar='"', quoting=csv.QUOTE_MINIMAL, delimiter=',',)
dialect = csv.register_dialect('pipe', delimiter='|')

with open('cars-original.csv', 'r') as source:
    reader = csv.reader(source, dialect='pipe')
    with open('cars.csv', 'w') as target:
        writer = csv.writer(target, dialect='comma_escaped')
        for row in reader:
            print(row)
            writer.writerow(row)
