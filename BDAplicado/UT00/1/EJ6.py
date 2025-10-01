num = int(input("Introduce un número: "))
medida = input("La unidad de medida es (mm, cm, m, km): ")

numInicial = num

match medida:
    case "mm":
        num = num
    case "cm":
        num = num * 10
    case "m":
        num = num * 1000
    case "km":
        num = num * 1000000
    case _:
        print("Opción no válida")

print("-------------------------------------------")
print("\n")
print("Elige la unidad a la que quieres convertir:")
print("\n")
print("1. Milimetros (mm)")
print("2. Centimetros (cm)")
print("3. Metros (m)")
print("4. Kilometros (km)")
op = input("Elige una opción: ")

match op:
    case "mm":
        print(f"{numInicial} {medida} son: son {num / 1} mm")
    case "cm":
        print(f"{numInicial} {medida} son: son {num / 10} cm")
    case "m":
        print(f"{numInicial} {medida} son: son {num / 1000} m")
    case "km":
        print(f"{numInicial} {medida} son: son {num / 1000000} km")
    case _:
        print("Opción no válida")