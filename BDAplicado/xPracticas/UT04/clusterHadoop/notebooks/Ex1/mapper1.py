#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue
    line = line.strip().split(",")
    generos = line[3]
    print(f"{generos}")
