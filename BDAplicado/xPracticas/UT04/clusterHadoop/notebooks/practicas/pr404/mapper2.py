#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue
    line = line.strip().split(";")

    region = line[1]
    total = line[7]

    print(f"{region}\t{total}")
