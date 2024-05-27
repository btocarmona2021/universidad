# Asignatura: INTRODUCCIÓN A LA PROGRAMACIÓN
# TRABAJO PRÁCTICO: Listas - Tuplas
# Desarrollar programa py para cada uno de los siguientes ejercicios:
# Ejercicio 1: Cree una lista con los siguientes elementos:
# conex=[ "127.0.0.1","root","123456","nomina"]

# a) Escriba un programa que imprima todos los elementos de la lista y la longitud total de la lista
# conex
# b) Escriba un programa que imprima los elementos ordenados de la lista. (presentación
# c) cree otra lista con los elementos en orden inverso (desde el último al 1ero)
# d) Encuentre el elemento “root” de la lista y contar cuantos hay

conex = ["127.0.0.1", "root", "123456", "nomina", "root"]

print("a:) Ejercicio A ")


def imprime_lista(lista):
    for elemento in conex:
        print(elemento)


imprime_lista(conex)
print("b:) Ejercicio B ")
conex.sort()

imprime_lista(conex)
print("c:) Ejercicio C ")

lista_ordenada = conex.reverse()
imprime_lista(lista_ordenada)

print("d:) Ejercicio D ")

print(f"El elemento root se encuentra {conex.count('root')} veces")  # primer forma
contador = 0
for elem in conex:
    if elem == 'root':
        contador = contador + 1

print(f"El elemento root se encuentra {contador} veces") # segunda forma
