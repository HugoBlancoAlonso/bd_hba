#!/usr/bin/env python3

import sys

total = 0
errores = 0

for line in sys.stdin:
    total = total + 1

    line = line.strip().split(",")
    url = line[0]
    codigo = str(line[1])

    if "error" in codigo:
        errores = errores + 1

print(f"ERRORES TOTALES: {(errores / total) * 100}%")
