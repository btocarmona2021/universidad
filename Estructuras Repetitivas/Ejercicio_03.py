"""
Ejercicio 3
Leer un número X y una secuencia de números. Mostrar cuál es el porcentaje de números leídos
que fueron múltiplos de X. Utilizar ciclo iterativo.
Ejemplo: X= 8 y la secuencia 12, 23, 24, 56, 11, 16, la salida es: 50

"""
import random

numero_x = random.randint(1, 10)
print(f"El numero elegido es el:{numero_x}")
numeros = int(input("ingrese la cantidad de numeros de la secuencia-> "))

rango_secuencia = int(input("ingrese el rango de numeros que se generarán-> "))

multiplos = 0
contador_secuencia = 1

for secuencia in range(0, numeros):
    numeros_aleatorios = random.randint(1, rango_secuencia)
    print(f"Secuencia Nº {contador_secuencia} genero el {numeros_aleatorios}")
    contador_secuencia += 1
    if numeros_aleatorios % numero_x == 0:
        multiplos += 1
        print("===================================================")
        print(f"-> {numeros_aleatorios} es multiplo de {numero_x}")
        print("===================================================")

print(f"La secuencia de {numeros} numeros tiene como multiplos de {numero_x} a {multiplos} numeros"
      f" lo que representa el {(multiplos / numeros) * 100} %")
