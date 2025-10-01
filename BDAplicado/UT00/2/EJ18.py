cad1 = input("Introduce la primera cadena: ")
rotar = int(input("Introduce el número de posiciones a rotar: "))

cad1 = [i for i in cad1]

for i in range(rotar):
    letra = cad1.pop(0)
    cad1.append(letra)

print("".join(cad1))