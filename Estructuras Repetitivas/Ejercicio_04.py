"""
Ejercicio 4
Escribir los números positivos MENORES a N, donde N es un número solicitado al usuario
"""

numero_N = int(input("Ingrese un numero y te daré todos los numeros menor al mismo->"))

for resultado in range(numero_N-1, 0, -1):
    print(resultado)

