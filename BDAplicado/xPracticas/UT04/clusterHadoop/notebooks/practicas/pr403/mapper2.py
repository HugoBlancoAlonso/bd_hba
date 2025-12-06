#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()
    ip = line[0]
    if line[9] == "-":
         bytes = 0
    else:
        bytes = int(line[9])

print(f"{ip}, {bytes}")
