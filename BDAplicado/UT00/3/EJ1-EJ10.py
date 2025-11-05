nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]


# 1

# nombres.sort()
# print(nombres)


# 2

# contador = len([nombre for nombre in nombres if nombre.startswith("A")])
# print(contador)


# 3

# nombreUsu = input("Introduce tu nombre: ")

# if nombreUsu in nombres:
#     print("Tu nombre está en la lista en la posicion", nombres.index(nombreUsu) + 1)
# else:
#     print("Tu nombre no está en la lista")


# 4

# nombre = input("Introduce un nombre: ")
# if nombre in nombres:
#     print(nombres[:nombres.index(nombre)])
# else:
#     print("El nombre", nombre, "no está en la lista")


# 5

# longitud = int(input("Introduce una longitud: "))
# lista = [nombre for nombre in nombres if len(nombre) == longitud]
# print("Hay", len(lista), "nombres con ", longitud, "caracteres.")



# 6

# lista = [nombre for nombre in nombres if len(nombre) < 5]
# print(lista)


# 7

# vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
# for nombre in nombres:
#     for vocal in vocales:
#         if vocal in nombre.lower():
#             vocales[vocal] += 1

# print("""
# A: {a}
# E: {e}
# I: {i}
# O: {o}
# U: {u}
# """.format(**vocales)) 


# 8

#letras = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

# letras = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, 
#           "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, 
#           "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, 
#           "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
# for nombre in nombres:
#     for i in range(len(nombre)):
#         letra = nombre[i].lower()
#         if letra in letras:
#             letras[letra] += 1

# print(letras)


# 9

# import random
# listaNumeros = []
# for i in range(10):
#     listaNumeros.append(random.randint(1, 100))
# suma = sum(listaNumeros)
# print(listaNumeros)
# print("La suma es:", suma)


# 10   

# palabras = ["agua", "luz", "agua", "fuego", "sol", "sol", "agua"]

# palabraUsu = input("Introduce una palabra: ")
# if palabraUsu in palabras:
#     print("La palabra", palabraUsu, "aparece", palabras.count(palabraUsu), "veces.")


# 16

# l1 = [1, 3, 4, 7, 8]
# l2 = [2, 3, 5, 6, 8]
# l3 = []

# for num in l1:
#     if num in l2:
#         l3.append(num)

# print(l3)    