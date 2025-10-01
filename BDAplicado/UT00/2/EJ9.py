palabra = input("Introduce una palabra: ")

def frecuencia_caracteres(cadena):
    frecuencias = {}
    for caracter in cadena:
        if caracter == " ":
            continue
        elif caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

frecuencias = frecuencia_caracteres(palabra)
for caracter, frecuencia in frecuencias.items():
    print(f"El carácter '{caracter}' aparece {frecuencia} veces.")