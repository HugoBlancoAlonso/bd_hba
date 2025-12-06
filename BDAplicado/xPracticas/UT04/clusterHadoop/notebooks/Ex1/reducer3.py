#!/usr/bin/env python3

import sys

dicTotal = {}
dicP = {}

for line in sys.stdin:
    line = line.strip().split(",")
    pais = line[0]
    presu = float(line[1])
    ing = float(line[2])

    ben = ing - presu

    if pais in dicP:
        dicP[pais] = dicP[pais] + 1
    else:
        dicP[pais] = 1

    if pais in dicTotal:
        dicTotal[pais] = dicTotal[pais] + ben
    else:
        dicTotal[pais] = ben

    for pais, count in dicP.items():

        if pais in dicTotal:
           dicTotal[pais] =  dicTotal[pais] / count

for pais, ben in dicTotal.items():
    print(f"{pais}: {ben}")
