#!/usr/bin/env python3

import sys

actual = None
mayorv = 0
año = 0

for line in sys.stdin:
    line = line.strip().split("\t")

    pais = line[0]
    yv = line[1]

    if actual == None:
        actual = pais

    if pais == actual:
        yv = yv.split(",")
        y = yv[0]
        v = float(yv[1])

        if v >= mayorv:
            mayorv = v
            año = y

    elif pais != actual:
        print(f"{actual} {año} ({mayorv})")
        actual = pais
        mayorv = 0
        año = 0

if actual is not None:
    print(f"{actual} {año} ({mayorv})")
