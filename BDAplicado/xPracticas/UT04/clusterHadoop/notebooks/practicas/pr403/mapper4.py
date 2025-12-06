#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()
    http = line[5]
    print(f"{http}, {1}")
