#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()
    url = line[6]

    print(f"{url}, {1}")
