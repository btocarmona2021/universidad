"""
Ejercicio 8

Crear un programa que permita al usuario procesar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

Si ingresa un monto negativo, no se debe procesar y se debe pedir que proporcione un nuevo monto.
 Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superar el total del $1000, se debe
aplicar un 10% de descuento.

"""

monto = int(input("por favor ingrese un monto-> "))
total = 0
descuento = False
des_obtenido = 0

while monto != 0:

    if monto < 0:
        while monto < 0:
            monto = int(input("El valor no puede ser negativo reingrese un monto"))

    total += monto
    monto = int(input("Ingrese un nuevo monto-> "))
if total > 1000:
    des_obtenido = total * 10 / 100
    total = total - (total * 10) / 100
    descuento = True

if descuento:
    lectura= "se"
else:
    lectura= "no se"

print(f"El monto a pagar es de {total} {lectura} aplicó descuento (ahorró {des_obtenido} pesos.)")
