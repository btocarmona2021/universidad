"""
Ejercicio 9

a) Desarrollar una función que indique si un determinado entero es un número primo.
Desde el programa principal: ingrese 25 números enteros e imprima un mensaje indicando si es o no primo
(llamando a la función) y el promedio de todos los números ingresados.

b) Desarrolle el punto a) utilizando ciclo INDEFINIDO. Utilizando los procedimientos anteriores ingrese
distintos números enteros por teclado hasta ingresar el número (0) que actuaría de corte.

"""


def es_primo(dato):
    for numero in range(2, valor - 1):
        calculo = valor % numero
        if calculo == 0:
            print("no es primo")
            return
    print("Es primo")


contador = 0
suma = 0
while True:
    valor = int(input("Ingrese un valor-> "))
    if valor == 0:
        break
    es_primo(valor)
    contador += 1
    suma += valor

print(f"El promedio de los {contador} numeros ingresados es {suma/contador}")
