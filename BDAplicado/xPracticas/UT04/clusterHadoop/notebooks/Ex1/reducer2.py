#!/usr/bin/env python3

import sys

maxnum = 0
maxgen = None

for line in sys.stdin:
    line = line.strip().split(",")
    gen = line[0]
    num = int(line[1])

    if num > maxnum:
        maxnum = num
        maxgen = gen

print(f"{maxgen}: {maxnum}")
