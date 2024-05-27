# Ejercicio 3:
# a) Armar una lista con números enteros positivos entre 0 y 20.
# b) Armar una lista entre 0 y 20 con múltiplos de 2
# c) Armar una lista entre 0 y 20 con múltiplos de 5 y además emitir un mensaje con la cantidad
# de números impares.
# d) Generar una lista con los N primeros términos de la sucesión de Fibonacci, por ejemplo si el
# número es 6 debe imprimir: 1 1 2 3 5 8.

lista_numeros = []

lista_Fibonacci = []


def arma_lista(multiplo=1, impares=False):
    lista_impares = []
    for i in range(0, 21, multiplo):
        lista_numeros.append(i)
    if impares:
        for numero in lista_numeros:
            if numero % 2 == 1:
                lista_impares.append(numero)
        print(f"Los numeros impares en la lista de los multiplos de 5 son: {lista_impares}")


arma_lista()
print(lista_numeros)

lista_numeros.clear()
arma_lista(2)
print(lista_numeros)

lista_numeros.clear()
arma_lista(5, True)

valor = int(input("Ingrese el numero a calcular la sucesión de Fibonacci"))

