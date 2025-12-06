#!/usr/bin/env python3

import sys

dic = {}

for line in sys.stdin:
    line = line.strip().split(",")
    ip = line[0]
    bytes = int(line[1])

    if ip in dic:
        dic[ip] = dic[ip] + bytes
    else:
        dic[ip] = bytes

for ip, bytes in dic.items(): 
    print(f"{ip}: {bytes} bytes")
