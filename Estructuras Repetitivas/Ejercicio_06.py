"""
Ejercicio 6

Escriba un procedimiento/función CartelMayor que muestre por pantalla la frase “es un número
mayor que cincuenta”
y un procedimiento CartelMenor que muestre por pantalla la frase “es un
número menor que cincuenta”.

Utilizando los procedimientos anteriores ingrése distintos números enteros por teclado hasta ingresar
el número (-1) que actuaría de corte.
Luego muestre por pantalla los carteles adecuados.
Halle e imprima la suma de todos los números menores de cincuenta.
"""


def cartel_mayor():
    print("es un número mayor que cincuenta")


def carte_menor():
    print("es un número menor que cincuenta")


valor =0
acumulador = 0

while valor != -1:

    valor = int(input("Por favor ingrese un numero entero (Ingrese -1 para salir)-> "))

    if valor > 50:
        cartel_mayor()

    if 0 < valor < 50:
        carte_menor()
        acumulador += valor

print(f"Los numeros ingresados que son menores a 50 se sumaron y dan como resultado: {acumulador}")
