"""
Ejercicio 10

Escribir una función que , dado un número de DNI, retorne True si el número es válido y False si no lo es.

Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
Permita que el usuario ingrese distintos
DNI por teclado hasta ingresar el número (-1) que actuaría de corte.

"""


def dni_valido(numero):
    contador = 0
    for digitos in numero:
        contador = + contador + 1
    if 6 < contador >= 8:
        return True
    else:
        return False


dni = str(input("Ingrese un numero de DNI-> "))

while dni != -1:

    if dni_valido(dni):
        print(f"¡ Genial el Dni {dni} es válido !")
    else:
        print(f"lo siento el dni {dni} NO es válido")

    dni = str(input("Ingrese un nuevo numero de DNI-> "))
