#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()
    navegador = line[11]
    print(f"{navegador}, {1}")
