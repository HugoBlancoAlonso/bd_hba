num = int(input("Introduce un número: "))

fact = 1
for i in range(num):
    fact *= i + 1

print(f"El factorial de {num} es {fact}")