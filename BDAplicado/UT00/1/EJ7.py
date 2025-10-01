import random as rd

num = rd.randint(1, 100)
print(num)

print("Adivina el número entre 1 y 100")
intento = int(input("Introduce un número: "))

while intento != num:
    if intento < num:
        print("El número es mayor")
    else:
        print("El número es menor")
    intento = int(input("Introduce un número: "))

print("¡Has acertado!")