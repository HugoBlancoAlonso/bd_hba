#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue

    line = line.strip().split(";")

    name = line[4]
    income = line[5]
    print(f"{income}\t{name}")
