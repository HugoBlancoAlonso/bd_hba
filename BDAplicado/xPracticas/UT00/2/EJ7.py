frase = input("Introduce una frase: ")

array = frase.split(" ")

frasefinal = ""

for i in range(len(array) - 1, -1, -1):
    frasefinal += array[i] + " "

print(frasefinal)