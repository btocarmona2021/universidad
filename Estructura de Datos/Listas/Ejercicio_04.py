# Ejercicio 4: Arme una lista con el factorial de un número N, ingresado por teclado. Ejemplo: 4!
# =4x3x2x1.


numero_factorizar = int(input("Ingrese el numero a factorizar-> "))

lista_factorial = []
for fact in range(numero_factorizar, 1, -1):
    print(fact)
    lista_factorial.append(f"{fact}x{fact-1}")
print(lista_factorial)

