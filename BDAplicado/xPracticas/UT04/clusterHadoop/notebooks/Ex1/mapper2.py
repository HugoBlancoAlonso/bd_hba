#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split(":")
    gen = line[0]
    num = int(line[1])
    num = f"{num:05d}"
    print(f"{gen}, {num}")
