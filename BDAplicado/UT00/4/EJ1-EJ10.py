# 1


# buscar = input("Ingrese el nombre de la fruta que desea buscar: ").strip().lower()

# frutas = {"manzana": 2, "banana": 5, "pera": 3, "kiwi": 4}

# if buscar in frutas:
#     print(f"La fruta {buscar} tiene un precio de {frutas[buscar]}.")
# else:
#     print(f"La fruta {buscar} no está en la lista.")
#     accion = input("Quieres añadir esta fruta a la lista? (s/n): ").strip().lower()
#     if accion == "s":
#         precio = float(input("Introduce el precio de la fruta: "))
#         frutas[buscar] = precio

# print(frutas)


# 2

# productos = {
#     "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
#     "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
#     "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
#     "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
#     "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
# }

# total = 0
# print("Catergorias disponibles:", len(productos))
# for categoria in productos:
#     print(f"-{categoria}: {len(productos[categoria])} productos")
#     total += len(productos[categoria])
# print("Total de productos:", total)


# 3

# frase = input("Ingrese una frase: ").lower()
# palabras = frase.split()
# frecuencias = {}

# for palabra in palabras:
#     if palabra in frecuencias:
#         frecuencias[palabra] += 1
#     else:
#         frecuencias[palabra] = 1

# for palabra, frecuencia in frecuencias.items():
#     print(f"{palabra}: {frecuencia}")


# 4


# asignaturas = {
#     "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
#     "Física": ["Elena", "Luis", "Juan", "Sofía"],
#     "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
#     "Historia": ["María", "Juan", "Elena", "Ana"],
#     "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
# }


# print("1. Listar estudiantes matriculados en una asignatura")
# print("2. Matricular un estudiante en una asignatura")
# print("3. Dar de baja un estudiante de una asignatura")

# opcion = int(input("Elige una opción (1-3): "))

# match opcion:
#     case 1:
#         asignatura = input("Introduce el nombre de la asignatura: ").strip().title()
#         if asignatura in asignaturas:
#             print(f"Estudiantes matriculados en {asignatura}: {', '.join(asignaturas[asignatura])}")
#         else:
#             print("No existe esa asignatura")
#     case 2:
#         asig = input("Introduce el nombre de la asignatura: ").strip().title()
#         estudiante = input("Introduce el nombre del estudiante: ").strip().title()
#         if asig in asignaturas:
#             asignaturas[asig].append(estudiante)
#             print(asignaturas[asig])
#         else:
#             print("No existe esa asignatura")
#     case 3:
#         asig = input("Introduce el nombre de la asignatura: ").strip().title()
#         estudiante = input("Introduce el nombre del estudiante: ").strip().title()
#         if asig in asignaturas:
#             if estudiante in asignaturas[asig]:
#                 asignaturas[asig].remove(estudiante)
#                 print(asignaturas[asig])
#             else:
#                 print("No existe ese estudiante en esa asignatura")
#         else:
#             print("No existe esa asignatura")


# 5

# diccionario1 = {"Nombre": "Juan", "Edad": 30, "Ciudad": "Madrid"}
# diccionario2 = {}

# for clave, valor in diccionario1.items():
#     diccionario2[valor] = clave
# print(diccionario1)
# print(diccionario2)


# 6

# productos1 = {"manzana": 2, "banana": 5, "pera": 3, "kiwi": 4}
# productos2 = {"banana": 4, "pera": 2, "naranja": 6, "manzana": 5}

# for producto, precio in productos1.items():
#     if producto in productos2:
#         productos2[producto] = (productos2[producto] + precio)
#     else:
#         productos2[producto] = precio

# print(productos1)
# print(productos2)


# 7

# empleados = {"Jose": 3000, "Ana": 3500, "Luis": 2800, "Marta": 4000, "Carlos": 3200}

# for nombre, salario in empleados.items():
#     if salario <= 3000:
#         print("Empleado con salario menor a 3000:", nombre)


# 8

departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}

op = 0

while op < 3:
    print("1. Lista de empleados de un departamento")
    print("2. Añadir un empleado a un departamento")
    print("3. Eliminar empleado")
    print("4. Salir")

    op = int(input("Elige una opción (1-4): "))

    match op:
        case 1:
            depart = input("Introduce el nombre del departamento: ").strip().title()
            if depart in departamentos:
                print(f"Empleados en {depart}:")
                for empleado, puesto in departamentos[depart].items():
                    print(f"- {empleado}: {puesto}")
            else:
                print("No existe ese departamento")