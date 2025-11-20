palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

anagrama = False

for char in palabra1:
    if char in palabra2:
        anagrama = True
    else:
        anagrama = False
        break

if anagrama:
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")