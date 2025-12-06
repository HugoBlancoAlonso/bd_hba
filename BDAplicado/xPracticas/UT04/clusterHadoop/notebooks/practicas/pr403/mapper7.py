#!/usr/bin/env python3

import sys

codigo = None

for line in sys.stdin:
    line = line.strip().split()
    url = line[6]
    cod = int(line[8])

    if cod >= 400:
        codigo = "error"
    else:
        codigo = "ok"

    print(f"{url}, {codigo}")
