"""Ejercicio 7: Dados dos números X e Y, diseñe un algoritmo que calcule
qué porcentaje es X de Y. Mostrar el resultado por pantalla.
Ejemplo 1: si X=10 e Y=100 entonces X es el 10% de Y.
Ejemplo 2: si X=120 e Y=100 entonces X es el 120% de Y.11)
"""
# si invierto los valores siempre sacara del mas chico con respecto al mas grande
x = 100
y = 500


# La funcion se encarga de recibir dos valores , determina cual es el menor y saca el porcentaje con respecto al mayo
def calcula_porcentaje(x, y):
    if x < y:
        resultado = (x / y) * 100
        return "El porcentaje del valor", x, " de ", y, "es de", resultado, "%"
    else:
        resultado = (y / x) * 100
        z = x
        x = y
        y = z
        return "El porcentaje del valor", x, " de ", y, "es de", resultado, "%"


# Llamo a la funcion la cual retorna un String con todos los valores del resultado
print(calcula_porcentaje(x, y))
