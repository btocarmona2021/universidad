"""Ejercicio 1
a) Construya un programa que lea los 10 primeros números naturales y determinar su suma."""


# Objetivo del problema es obtener los 10 primeros numeros naturales.
# Datos relevantes : 10 numeros naturales.


def numeros_naturales():
    for naturales in range(0, 10):
        imprime_numeros(naturales)


def imprime_numeros(natural):
    print(f"El numero natural es: {natural}")


numeros_naturales()
