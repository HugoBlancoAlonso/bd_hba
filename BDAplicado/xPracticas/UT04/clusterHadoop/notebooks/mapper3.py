#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:
    if first:
        first = False
        continue
    line = line.strip().split(",")
    presu = float(line[9])
    ing = float(line[10])
    pais = line[11]
    print(f"{pais},{presu},{ing}")
