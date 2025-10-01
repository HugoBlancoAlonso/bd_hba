cad = input("Introduce una cadena: ")

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

cantv = 0
cantc = 0

for char in cad:
    if char == ' ':
        continue
    elif char in vocales:
        cantv += 1
    else:
        cantc += 1

print(f"Cantidad de vocales: {cantv}")
print(f"Cantidad de consonantes: {cantc}")