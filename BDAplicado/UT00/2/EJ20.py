frase = input("Introduce una palabra: ")
hayvocal = False
fraseFinal = ""
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in frase:
    for vocal in vocales:
        if char == vocal:
            hayvocal = True
    if hayvocal:
        fraseFinal += "*"
    else:
        fraseFinal += char
    hayvocal = False
    

print(fraseFinal)