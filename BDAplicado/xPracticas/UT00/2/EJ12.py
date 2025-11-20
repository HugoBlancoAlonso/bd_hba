palabra = input("Introduce una palabra: ")

rle = ""

anterior = palabra[0]

cont = 0
for char in palabra:
    if char != anterior:
        rle += anterior+str(cont)
        anterior = char
        cont = 1
    else:
        cont += 1
        anterior = char


if cont == 1:
    rle += palabra[-1]+str(cont)
else:
    rle += palabra[-1]+str(cont)


print(rle)
