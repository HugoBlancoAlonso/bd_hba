import re

frase = input("Introduce una frase: ")
frase = frase.title()
frase = frase.replace("-", " ")
frase = frase.replace(" ", "")
frase = frase[0].lower() + frase[1:]

print(frase)
            
            