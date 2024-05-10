"""
Ejercicio 9

a) Desarrollar una función que indique si un determinado entero es un número primo.
Desde el programa principal: ingrese 25 números enteros e imprima un mensaje indicando si es o no primo
(llamando a la función) y el promedio de todos los números ingresados.

b) Desarrolle el punto a) utilizando ciclo INDEFINIDO. Utilizando los procedimientos anteriores ingrese
distintos números enteros por teclado hasta ingresar el número (0) que actuaría de corte.

"""


#
# def numero_primo(valor):
#     if  valor / valor == 1
#

def es_primo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(es_primo(4))
