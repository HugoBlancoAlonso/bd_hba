#!/usr/bin/env python3

import sys

c_ciudad = None
ciudad = None
c_año = 0
año = 0
c_temp = 0
temp = 0
count = 0

for line in sys.stdin:
    line = line.strip().split("\t", 2)
    ciudad = line[0]
    año = line[1]
    temp = float(line[2])

    if c_ciudad == None:
        c_ciudad = ciudad
        c_año = año
        if ((temp - 32) * 5 / 9) >= 30:
            count += 1
    elif ciudad == c_ciudad:
        if año == c_año:
            if ((temp - 32) * 5 / 9) >= 30:
                count += 1
        else:
            print(f"{c_ciudad} ({c_año}) ---> {count}")
            c_año = año
            if ((temp - 32) * 5 / 9) >= 30:
                count = 1
            else:
                count = 0

    else:
        print(f"{c_ciudad} ({c_año}) ---> {count}")
        c_ciudad = ciudad
        c_año = año
        if ((temp - 32) * 5 / 9) >= 30:
            count = 1
        else:
            count = 0

if ciudad is not None:
    print(f"{ciudad} ({c_año}) ---> {count}")
