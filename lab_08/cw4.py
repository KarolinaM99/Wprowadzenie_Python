from collections import namedtuple
import csv

with open('zamowienia.csv', newline='', encoding="utf8",errors="ignore") as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    Line = namedtuple('Line', [x.replace(" ","_") for x in next(reader, None)])
    list_of_lines = list()
    for _ in range(15):
        list_of_lines.append(Line._make(next(reader, None)))
        for x in list_of_lines:
            print(x)