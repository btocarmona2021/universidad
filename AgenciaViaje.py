""" Venta de Pasajes"""
# Tenemos que armar un software para calcular el precio de un pasaje
# Dado la distancia, y el precio por kilometro.


destinos = ["San Antonio", "General Roca", "Bariloche", "Valcheta", "Jacobacci"]
distancias = [175, 600, 800, 250, 500]

precio = 100


def confPrecio(valor):
    print(f"El precio actual configurado es {valor}")
    precio = int(input("Ingrese nuevo valor por kilometros"))
    return precio


def imprimir_destinos(destinos):
    for indice, destino in enumerate(destinos):
        print(indice, destino)


def calcular_precio(dest, dist, prec):
    imprimir_destinos(dest)
    iddestino = int(input(f"Seleccion un destino de  0 a {len(destinos) - 1} -> "))
    precio_pasaje = dist[iddestino] * prec
    print(f"Un pasaje a {dest[iddestino]} cuesta {precio_pasaje}")


def agregar_detino():
    nueva_ciudad = input("Ingrese el nuevo destino-> ")
    destinos.append(nueva_ciudad)
    distancias.append(int(input("Ingrese la distancia en kilometros hacia " + nueva_ciudad + " -> ")))


while True:
    print("╔═══════════════════════════════╗")
    print("║       ELIJA UNA OPCION        ║")
    print("╚═══════════════════════════════╝")
    print("╔═══════════════════════════════╗")
    print("║  a) Mostrar precio actual     ║")
    print("║  b) Configurar el precio act  ║")
    print("║  c) Calcular Precio           ║")
    print("║  d) Agregar un destino        ║")
    print("║  e) Salir                     ║")
    print("╚═══════════════════════════════╝")
    opcion = input("Elije una opcion (a) (b) (c) (d) (e)-> ")

    if opcion == "a":
        print(f"El precio actual configurado es $ {precio}")
    elif opcion == "b":
        precio = confPrecio(precio)
    elif opcion == "c":
        calcular_precio(destinos, distancias, precio)
    elif opcion == "d":
        agregar_detino()
    else:
        print("opcion incorrecta")
