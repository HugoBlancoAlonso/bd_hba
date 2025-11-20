import math

num = 0
while num % 2 == 0:
    num = int(input("Introduce un número impar: "))

cadena = ""
for i in range(math.ceil(num/2)):
    for j in range(num - i - 1):
        cadena += " "
    for k in range(2*i+1):
        cadena += "*"
    cadena += "\n"

print(cadena)