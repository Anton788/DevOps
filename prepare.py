#!/usr/bin/env python3
import sys
import csv
from datetime import datetime


def preparing_data(data):
    total = data[0]
    usage = data[1]
    free = data[2]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    usage_perc = int(int(usage) * 100 / int(total))
    with open("monitoring.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([current_time, total, free, usage_perc])


for line in sys.stdin:
    parts = line.split()
    if len(parts) > 0 and parts[0] == "Total:":
        preparing_data(parts[1:])
