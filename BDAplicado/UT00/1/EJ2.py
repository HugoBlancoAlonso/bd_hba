numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Cuantos multiplos de " + str(numero1) + " quieres: "))

for i in range(1, numero2 + 1):
    print(str(numero1) + " * " + str(i) + " = " + str(numero1 * i))
