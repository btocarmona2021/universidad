"""Ejercicio 6: Dada como entrada la temperatura en Grados Centígrados (G), obtenga la temperatura
Fahrenheit equivalente utilizando la siguiente fórmula: F = (9/5) * G +32. Mostrar el resultado por pantalla."""


# Funcion con la cual convierto la temperatura en grados a Fahrenheit
def devuelve_fahrenheit(temp):
    return (9 / 5) * temp + 32

#Solicito al usuario que ingrese la temeperatura expresada en Grados
temperatura_grados = int(input("Ingrese la temperatura actual en grados centigrados-> "))

#Llamo a la funciona la cual me retorna los grados expresados en Fahrenheit
print("La temperatura actual expresada en Fahrenheit es de: ", devuelve_fahrenheit(temperatura_grados), " F")
