cad1 = input("Introduce la primera cadena: ")
cad2 = input("Introduce la segunda cadena: ")

asci1 = [ord(i) for i in cad1]
asci2 = [ord(i) for i in cad2]


if sum(asci1) > sum(asci2):
    print(f"La cadena con mayor valor ASCII es: {cad1}, con un valor de {sum(asci1)}")
else:
    print(f"La cadena con mayor valor ASCII es: {cad2}, con un valor de {sum(asci2)}")

