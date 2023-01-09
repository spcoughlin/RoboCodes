import datetime

import openpyxl
import time

wb = openpyxl.Workbook()
now = datetime.datetime.now()
dest_filename = f"hours_table_{now}.xlsx"

ws1 = wb.active

names, hours = [], []
for i in range(65):
    with open(f"HoursFiles/hoursfile{i}.txt", "r") as f:
        lines = f.readlines()
        names.append(lines[0][:-1])
        hours.append(lines[1][:-1])

for i in range(1, len(names)):
    ws1[f"A{i}"] = names[i]
    ws1[f"B{i}"] = hours[i]

wb.save(filename=dest_filename)