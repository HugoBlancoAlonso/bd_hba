import math

nums = []

for i in range(5):
    nums.append(int(input("Introduce un número: ")))


mayor = math.inf * -1
menor = math.inf
for n in nums:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print(f"El mayor es {mayor} y el menor es {menor}")