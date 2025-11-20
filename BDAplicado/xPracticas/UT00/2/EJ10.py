import re

palabraLimpiar = input("Introduce una palabra: ")

def limpiar_palabra(palabra):
    palabra = re.sub(r'[^a-zA-Z]', '', palabra) 
    return palabra

palabra_limpia = limpiar_palabra(palabraLimpiar)
print(f"La palabra limpia es: {palabra_limpia}")