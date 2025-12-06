#!/usr/bin/env python3

import sys

for line in sys.stdin:
    pal, num = line.strip().split(",", 1)
    num = int(num)
    num = f"{num:05d}"
    print(f"{num}, {pal}")
