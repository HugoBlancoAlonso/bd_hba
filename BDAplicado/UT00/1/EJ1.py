def solicitar_numero():    
    while True:
        try:
            numero = int(input("Por favor, introduce un número: "))
            return numero
        except ValueError:
            print("Debes introducir un número válido.")

numero = solicitar_numero()
print(f"Has introducido el número: {numero}")