"""
Ejercicio 2:
Utilice las librería que crea necesario para:
a) posicionarse en el directorio Documentos, pero guarde el actual
b) ejecute el comando ls y colóquelo en una lista
c) cuente los archivos con nombre mayor a 6 caracteres
d) luego vuelva a directorio inicial
"""
import os

directorio_actual = os.getcwd()

os.chdir('C:\\Users\\Alberto\\Documents')
documentos = os.getcwd()
print(documentos)

os.system('dir')
lista_dir_arch = os.listdir()
print(lista_dir_arch)

cantidad = 0
for archivo in lista_dir_arch:
    print(archivo)
    if len(archivo) > 6:
        cantidad += 1
print(f'La cantidad de archivos mayores a 6 caracteres es de {cantidad}')
os.chdir(directorio_actual)
print(f'Volviendo al directorio actual {os.getcwd()}')
