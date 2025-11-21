#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue  # saltar cabecera
    line = line.strip().split(",")
    print(f"{line[3]}\t{line[7]}")

