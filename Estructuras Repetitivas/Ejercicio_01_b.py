"""b) Modifique el programa anterior para que muestre el promedio de los pares
y el promedio de los impares."""


def numeros_naturales():
    suma_pares = 0
    contador = 0
    resultado = 0

    for naturales in range(0, 10):
        if naturales % 2 == 0:
            contador += 1
            suma_pares += naturales
            resultado = suma_pares / contador

    imprime_resultado(resultado)


def imprime_resultado(resultado):
    print(f"el reultado promedio de la suma de los pares es {resultado}")


numeros_naturales()
