"""
Ejercicio 3:
Los siguientes programas contienen errores que impedirían ejecutarlos. Reescribe cada programa corrigiendo
los errores y describe brevemente cada error.
Ejercicio a)
"""
lista = []
for i in range(4):
    palabra = input('Dime una palabra')
    lista.append(palabra)
    print(f'Las palabras escritas son {lista}')

# Ejercicio b)
contador = 0
for i in range(3, 10):
    contador = contador + 1
    print(f'Por ahora contador vale {contador} pero todavía no he terminado')
print(f'En total, contador vale {contador}')
