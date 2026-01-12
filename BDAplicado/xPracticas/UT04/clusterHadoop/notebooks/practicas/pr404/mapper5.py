#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue

    line = line.strip().split(";")

    gdp = float(line[8])

    if gdp < 10000.00:
        print(f"Pequeña\t1")
    elif gdp < 100000.00:
        print(f"Mediana\t1")
    elif gdp >= 100000.00:
        print(f"Grande\t1")
