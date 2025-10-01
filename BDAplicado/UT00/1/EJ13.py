palabra = input("Introduce una palabra: ")

reversa = ""
for i in range(len(palabra)-1, -1, -1):
    reversa += palabra[i]

print(reversa)