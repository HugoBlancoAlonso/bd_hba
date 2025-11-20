palabra = input("Introduce una palabra: ")

reversa = ""
for i in range(len(palabra) - 1, -1, -1):
    reversa += palabra[i]

if palabra == reversa:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")