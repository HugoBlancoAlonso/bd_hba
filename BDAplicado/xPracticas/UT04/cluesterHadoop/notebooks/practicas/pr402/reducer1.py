#!/usr/bin/env python3

import sys

current_city = None
current_temperature = 0

for line in sys.stdin:
    city, temperature = line.strip().split("\t", 1)
    temperature = float(temperature)
    
    if current_city is None:
        current_city = city
        current_temperature = temperature
    elif city == current_city:
        if temperature > current_temperature:
            current_temperature = temperature
    else:
        print(f"{current_city} ---> {current_temperature}")
        current_city = city
        current_temperature = temperature

if current_city is not None:
    print(f"{current_city} ---> {current_temperature}")
