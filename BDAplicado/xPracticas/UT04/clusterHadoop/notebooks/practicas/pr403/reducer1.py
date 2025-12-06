#!/usr/bin/env python3


import sys

dic = {}

for line in sys.stdin:
    line = line.strip().split(", ")
    num = int(line[0])
    count = int(line[1])

    if num in dic:
        dic[num] = dic[num] + count
    else:
        dic[num] = count

for num, count in dic.items():
    print(f"{num}: {count}")
