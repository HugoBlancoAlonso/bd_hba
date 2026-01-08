#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue
    line = line.strip().split(";")

    year = line[6]
    name = line[4]
    variation = line[9]

    print(f"{name}\t{year},{variation}")
