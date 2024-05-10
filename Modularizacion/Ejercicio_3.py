"""Ejercicio 3: Escriba un programa que permita calcular la superficie de una forma simple (rectángulo, círculo,
triángulo y rombo). El mismo debe contener un menú que pregunte que forma se va a elegir y luego pide la
entrada correspondiente para cada fórmula. Por ejemplo:
1) Rectángulo
2) Círculo
3) Triángulo
4) Rombo
Si se ingresa 2, debería pedir el radio de un círculo y debería imprimir un mensaje: “La superficie de un círculo
de radio 4 es 50,24”
Usted debe diseñar una función para resolver cada forma del menú."""
import math

print("╔═══════════════════════════════╗")
print("║       ELIJA UNA OPCION        ║")
print("╚═══════════════════════════════╝")
print("╔═══════════════════════════════╗")
print("║  1) Rectángulo                ║")
print("║  2) Círculo                   ║")
print("║  3) Triángulo                 ║")
print("║  4) Rombo                     ║")
print("╚═══════════════════════════════╝")
opcion = int(input("Elije una opcion (1) (2) (3) (4)-> "))

if opcion == 1:
    lado_a = int(input("Ingrese el tamaño del lado A-> "))
    lado_b = int(input("Ingrese el tamaño del lado B-> "))
    print("La superficie del rectangulo es de", lado_a * lado_b)
elif opcion == 2:
    radio = float(input("Ingrese el radio del circulo "))
    print("La superficie del circulo con radio", radio, "es de", round(math.pi * radio * radio, 2))
elif opcion == 3:
    base = int(input("Ingrese el tamaño de la base del triangulo-> "))
    altura = int(input("Ingrese el tamaño de la altura del triangulo-> "))
    print("La superficie del triangulo es de", (base * altura) / 2)
elif opcion==4:
    diagonal_uno= int(input("ingrese el valor de la diagonal 1 del rombo-> "))
    diagonal_dos= int(input("ingrese el valor de la diagonal 2 del rombo-> "))
    print("La superficie del rombo es de", (diagonal_uno*diagonal_dos)/2, "unidades cuadradas")
else:
    print("La opcion elegida no es válida")
