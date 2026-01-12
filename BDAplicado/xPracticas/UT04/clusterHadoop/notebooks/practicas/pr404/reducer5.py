#!/usr/bin/env python3

import sys
tipos = {"Pequeña": 0, "Mediana": 0, "Grande": 0}

for line in sys.stdin:
    line = line.strip().split()
    tipo = line[0]
    num = int(line[1])

    if tipo == "Pequeña":
        tipos["Pequeña"] = tipos["Pequeña"] + num
    elif tipo == "Mediana":
        tipos["Mediana"] = tipos["Mediana"] + num
    elif tipo == "Grande":
        tipos["Grande"] = tipos["Grande"] + num

for nombre_tipo, total in tipos.items():
    print(f"{nombre_tipo}: {total}")
