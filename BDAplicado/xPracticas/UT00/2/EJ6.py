frase = input("Introduce una frase: ")

frasefinal = ""
for char in frase:
    if char == char.upper():
        frasefinal += char.lower()
    else:
        frasefinal += char.upper()

print(frasefinal)