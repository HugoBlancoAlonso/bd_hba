#!/usr/bin/env python3

import sys
import string

simbolos = str.maketrans('', '', string.punctuation + '¿¡»«')
dic1 = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
}
suprimir = ["de", "la", "el", "y", "en", "que", "a", "los", "del", "se"]
acentos = str.maketrans(dic1)

for line in sys.stdin:
    line = line.lower()
    line = line.translate(simbolos)
    line = line.translate(acentos)
    line = line.strip().split()
    for word in line:
        if word not in suprimir:
            print(f"{word}\t1")

