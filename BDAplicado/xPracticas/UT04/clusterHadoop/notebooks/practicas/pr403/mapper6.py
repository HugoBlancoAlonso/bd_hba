#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()
    
    fecha = line[3]
    fecha = fecha.strip().split(":")
    hora = fecha[1]
    print(f"{hora}, {1}")
