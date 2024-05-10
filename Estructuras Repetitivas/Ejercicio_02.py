"""
Ejercicio 2
Dado un número N calcular su factorial. Utilizar ciclo definido,
estructura For y variable acumuladora del producto.

Ejemplo: 4! =4*3*2*1 = 24

"""
producto = 0
n = int(input('Ingrese el valor del numero a calcular el Factorial-> '))


for j in range(n-1, 0, -1):
    producto += n * j
    print(producto)
