#!/usr/bin/env python3

import sys

dic = {}

for line in sys.stdin:
    line = line.strip().split(",")
    hora = line[0]
    count = int(line[1])
    if hora in dic:
        dic[hora] = dic[hora] + count
    else:
        dic[hora] = count

for hora, count in dic.items():
    print(f"{hora}, {count}")
