# Ejercicio 1:
# Utilizando estructura de repetición con ciclo indefinido, genere un menú que ofrezca la selección de las
# siguientes opciones
# a) armar una lista con 10 elementos generados al azar con la función random, elementos entre 0 y 100
# b) imprimir la lista ordenada
# c) hallar el porcentaje de los impares
# d) hallar la cantidad de números primos.
import random
import time

opcion = ""

numeros = []


def numeros_primos():
    primos = []
    for numero in numeros:
        if numero < 2:
            continue
        if numero == 2:
            primos.append(numero)
            continue
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)
    print(f" Hay {len(primos)} numeros primos")


def arma_lista():
    for _ in range(1, 5):
        numeros.append(random.randint(0, 10))
    print("se han generado los 10 numeros aleatorios entre 0 y 100")
    time.sleep(2)


def ordena_lista():
    numeros.sort()
    print("Numeros ordenados en forma ascendente")
    print(numeros)
    time.sleep(2)


def porcentaje_impares():
    contador = 0
    impares = []
    for numero in numeros:
        if numero % 2 != 0:
            contador += 1
            impares.append(numero)
    porcentaje = contador / len(numeros) * 100
    print(f"El porcentaje de los numeros impares es de {porcentaje} % {impares}")
    time.sleep(2)


while opcion.lower != "e":
    print("╔════════════════════════════════════════════╗")
    print("║             ELIJA UNA OPCION               ║")
    print("╚════════════════════════════════════════════╝")
    print("╔════════════════════════════════════════════╗")
    print("║  a) armar una lista con 10 elementos       ║")
    print("║  b) imprimir la lista ordenada             ║")
    print("║  c) Hallar el porcentaje de los impares    ║")
    print("║  d) Hallar la cantidad de números primos   ║")
    print("║  e) Salir del sistema                      ║")
    print("╚════════════════════════════════════════════╝")

    opcion = input("Elije una opcion (a) (b) (c) (d) (e)-> ")

    if opcion == "a":
        arma_lista()
    elif opcion == "b":
        ordena_lista()
    elif opcion == "c":
        porcentaje_impares()
    elif opcion == "d":
        numeros_primos()
    elif opcion == "e":
        print("Saliendo del sistema")
        time.sleep(2)
