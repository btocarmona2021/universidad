# 1. Ejercicio1
# a. Solicitar al usuario que ingrese números, los cuales se guardaran en una lista.
# Finalizar al ingresar el número 0, el cual no debe guardarse.
# b. Solicitar al usuario que ingrese un número y, si el numero ingresado está en la lista,
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

# c. Imprimir la sumatoria de todos los números de la lista

# d. Solicitar al usuario que ingrese otro número y crear una lista con los elementos de la
# lista original que sean menores que el número ingresado. Imprimir esta nueva lista,
# iterando por ella

# e. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una
# compuesta por un número de la lista original y la cantidad de veces que aparece en
# ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá
# [(5,3),(16,1),(2,2),(57,1)]

lista_numeros = []
numero = -1

while numero != 0:
    numero = int(input("Ingrese numeros, cuando desee dejar de ingresar presione 0-> "))
    if numero != 0:
        lista_numeros.append(numero)

numero_solicitado = int(input("Ingrese un numero a buscar-> "))

for existe in lista_numeros:
    eliminado = False
    if existe == numero_solicitado:
        eliminado = True
        break
if eliminado:
    print(f"Se ha eliminado el numero {numero_solicitado}")
else:
    print(f"El numero {numero_solicitado} no se pudo eliminar, no esta en la lista")


def imprimir_sumatoria(lista):
    sumatoria = 0
    for suma in lista:
        sumatoria += suma
    print(f"La suma de todos los numeros da {sumatoria}")


imprimir_sumatoria(lista_numeros)


otro_numero = int(input("Ingrese otro numero para crear una nueva lista con numeros menos al ingresado-> "))
nueva_lista = []
for number in lista_numeros:
    if otro_numero > number:
        nueva_lista.append(number)
print(f"La nueva lista contiene todos los numeros menores a {otro_numero} ellos son: {nueva_lista}")

#me falta el punto E