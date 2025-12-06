#!/usr/bin/env python3

import sys

dic = {}

for line in sys.stdin:
    line = line.strip().split(",")
    http = line[0]
    count = int(line[1])

    if http in dic:
        dic[http] = dic[http] + count
    else:
        dic[http] = count

for http, count in dic.items():
    print(f"{http}, {count}")
