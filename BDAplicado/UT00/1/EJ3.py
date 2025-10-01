num = int(input("Introduce un número: "))

cadena = ""
for i in range(1, num + 1):
    for j in range(i):
        cadena += "*"
    cadena += "\n"

print(cadena)