"""
Ejercicio 5
Ingresar dos números a y b. retornar la suma de los números impares naturales que hay entre ellos.
Este problema se resuelve con ¿ciclo definido o indefinido?

Ejemplo: a=4 y b= 12, el cálculo es 5+7+9+11 y la salida es: 32.
"""

numero_a = int(input("Ingrese un numero positivo-> "))
numero_b = int(input("Ingrese un numero positivo mayor al ingresado anteriormente-> "))

acumulador = 0
contador = 1

for impares in range(numero_a, numero_b, 1):

    if  impares % 2 == 1:
        acumulador = acumulador + impares
        contador += 1
        print(f"El numero impar {contador} es : {impares}")
print(f"La suma de los numeros impares es {acumulador}")
