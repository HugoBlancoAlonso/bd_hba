
import numpy as np
import matplotlib.pyplot as plt

num = int(input("Introduce un número: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Probar con algunos valores
for i in range(num):
    print(f"F({i}) = {fibonacci(i)}")


plt.plot([fibonacci(i) for i in range(num)], 'o-')
plt.title("Números de Fibonacci")
plt.show()
