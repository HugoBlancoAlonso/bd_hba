#!/usr/bin/env python3

import sys
import numpy as np

region = None
c_region = None
temp = 0
max = 0
min = 10000

for line in sys.stdin:
    line = line.strip().split("\t", 1)
    region = line[0]
    temp = float(line[1])

    if c_region == None:
        c_region = region
        max = temp
        min = temp

    elif c_region == region:
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
            
    else:
        print(f"---> {c_region}: MAX ({max}) MIN ({min})")
        c_region = region
        max = temp
        min = temp

if c_region is not None:
    print(f"---> {c_region}: MAX ({max}) MIN ({min})")
