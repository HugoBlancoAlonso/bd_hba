#!/usr/bin/env python3

import sys

actual = None
cont = 0
total = 0

for line in sys.stdin:
    line = line.strip().split()

    region = line[0]
    gdp = float(line[1])

    if actual == None:
        actual = region

    if region != actual:
        prom = total / cont

        print(f"{actual}: {prom}")
        actual = region
        total = gdp
        cont = 1

    if actual == region:
        total = total + gdp
        cont = cont + 1

if region is not None:
    prom = total / cont
    print(f"{actual}: {prom}")
