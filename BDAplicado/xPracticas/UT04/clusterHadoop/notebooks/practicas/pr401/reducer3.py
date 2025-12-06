#!/usr/bin/env python3

import sys

for line in sys.stdin:
    num, pal = line.strip().split(", ", 1)
    num = int(num)
    print(f"{num}, {pal}")
