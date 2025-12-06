#!/usr/bin/env python3

import sys

palabra = None
val = 0
dic = {}


for line in sys.stdin:
    line = line.strip().split("\t", 1)
    palabra = line[0]
    val = int(line[1])

    if palabra in dic:
        dic[palabra] = dic[palabra] + val
    else:
        dic[palabra] = val


for pal, val in dic.items():
    print(f"{pal},{val}")
