#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue
    line = line.strip().split(";")
    name = line[4]
    year = int(line[6])
    total = float(line[7])

    if year >= 2000 and total > 0:
        print(f"{name}\t{year}\t{total}")
