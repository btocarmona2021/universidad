"""Ejercicio 1: Los programas que se indican a continuación, en Python, no funcionan,
deberá determinar donde está el error y corregirlos. """


def mostrar(a, b):
    if (a > b):
        mensaje = a, " es mayor que ", b
        return mensaje
    else:
        mensaje = b, " es mayor que ", a
        return mensaje


a = input("Introduzca primer numero: ")
b = input("Introduzca segundo numero: ")

print(mostrar(a, b))
