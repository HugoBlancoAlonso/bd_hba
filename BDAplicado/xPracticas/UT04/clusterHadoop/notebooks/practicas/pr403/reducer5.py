#!/usr/bin/env python3

import sys

dic = {}

for line in sys.stdin:
    line = line.strip().split(",")
    line = line[0]
    if line in dic:
        dic[line] = dic[line] + 1
    else:
        dic[line] = 1

for line, count in dic.items():
    print(f"{line}, {count}")
