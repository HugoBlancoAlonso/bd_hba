palabras = input("Introduce una palabra: ")

def eliminar_caracteres_rep(palabra):
    resultado = ""
    charant = ""
    for char in palabra:
        if char != charant:
            resultado += char
        charant = char
    return resultado

print(eliminar_caracteres_rep(palabras))