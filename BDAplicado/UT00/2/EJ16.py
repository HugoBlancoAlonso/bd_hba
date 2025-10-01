cad1 = input("Introduce la primera cadena: ")
cad2 = input("Introduce la segunda cadena: ")

if len(cad1) > len(cad2):
    print(f"La cadena con mayor longitud es: {cad1}, con una longitud de {len(cad1)}")
else:
    print(f"La cadena con mayor longitud es: {cad2}, con una longitud de {len(cad2)}")