import math

num = int(input("Introduce un número: "))

if num < 2:
    print("No es primo")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")
    