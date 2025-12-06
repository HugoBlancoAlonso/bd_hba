#!/usr/bin/env python3

import sys

dic = {}

for line in sys.stdin:
    line = line.strip().split()
    url = line[0]
    count = int(line[1])

    if url in dic:
        dic[url] = dic[url] + count
    else:
        dic[url] = count

for url, count in dic.items():
    print(f"{url}, {count}")
