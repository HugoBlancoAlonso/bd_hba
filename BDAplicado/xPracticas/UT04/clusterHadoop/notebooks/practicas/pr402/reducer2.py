#!/usr/bin/env python3

import sys

c_pais = None
c_temp = 0
count = 0
total = 0
media = 0


for line in sys.stdin:
    pais, temp = line.strip().split("\t", 1)
    temp = float(temp)

    if c_pais == None:
        c_pais = pais
        c_temp = temp
        count += 1
    elif c_pais == pais:
        c_temp = temp
        count += 1
        total += c_temp
    else:
        media = total / count
        print(f"{c_pais} ---> {media:.2f}")
        c_pais = pais
        c_temp = temp
        media = 0 
        total = c_temp
        count = 1
        
if c_pais is not None:
    print(f"{pais} ---> {media:.2f}")
