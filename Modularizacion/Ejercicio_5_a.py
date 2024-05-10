"""Ejercicio 5: Escriba un programa que solicite al usuario un número entero y lo clasifique como positivo, negativo
o cero. Utiliza una función para realizar la clasificación del número, mostrar un mensaje en el programa
principal. Por ejemplo para el número 25 el mensaje sería: “El número 25 es positivo”"""

numero = float(input("Ingrese un numero , evaluaré si es positivo, negativo, o has ingresado 0-> "))


def comprueba_num(numero):
    if numero > 0:
        return "El numero es positivo"
    elif numero < 0:
        return "El numero es negativo"
    else:
        return "El numero ingresado es 0"


print(comprueba_num(numero))
