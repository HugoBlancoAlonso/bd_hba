import re

rle = input("Introduce una cadena: ")

letra = ""
numero = 0
palabra = ""

for char in rle:
    """
    if re.match(r"[a-zA-Z]", char):
        letra = char
    """
    if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letra = char
    else:
        numero = int(char)

    if numero != 0:
        for i in range(numero):
            palabra += letra
        numero = 0

print(palabra)