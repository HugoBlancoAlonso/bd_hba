#!/usr/bin/env python3

import sys

alto = set()
bajo = set()
medioBajo = set()
medioAlto = set()

for line in sys.stdin:
    line = line.strip().split("\t")
    income = line[0]
    pais = line[1]

    if income == "INGRESO ALTO":
        alto.add(pais)
    elif income == "PAÍSES DE INGRESO BAJO":
        bajo.add(pais)
    elif income == "PAÍSES DE INGRESO MEDIANO BAJO":
        medioBajo.add(pais)
    elif income == "INGRESO MEDIANO ALTO":
        medioAlto.add(pais)

print(f">> Ingreso Alto: {alto}")
print(f">> Ingreso Medio Alto: {medioAlto}")
print(f">> Ingreso Medio Bajo: {medioBajo}")
print(f">> Ingreso Bajo: {bajo}")
