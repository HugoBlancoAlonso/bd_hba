#!/usr/bin/env python3

import sys

dic = {}

for line in sys.stdin:
    line = line.strip().split(";")

    for gen in line:
        if gen != "":
            if gen in dic:
                dic[gen] = dic[gen] + 1
            else:
                dic[gen] = 1


for gen, count in dic.items():
    print(f"{gen}: {count}")
