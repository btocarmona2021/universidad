import os, sys, platform

"""
Problema 1:
a) Mostrar en pantalla el directorio actual
b) dar un mensaje si existe o no un directorio (use como ejemplo: /home).
Utilizaremos: os.path.exists(path))
"""

directorio = os.getcwd()
print(directorio)
contenido = os.listdir()
print(contenido)
print()
path = input("ingrese el directorio a cambiar")

print("")
os.chdir(path)
print(os.getcwd())

"""
Problema 2:
a) Mostrar en pantalla el número de versión de Python sys.version
b) mostrar la longitud de la cadena resultante en a)
c) convertir esa cadena en una lista de elementos
d) mostrar el 1er y el último elemento de la lista anterior
"""

version = sys.version
print(version)
print(f"la canttidad de caracteres es de {len(str(version))} ")

lista_caracteres = []

# for caracteres in version:
#     lista_caracteres.append(caracteres)
# print(lista_caracteres)

lista_caracteres = list(version)

print(lista_caracteres)


"""
Problema 3:
Indicar con un mensaje si el sistema operativo de la computadora es “Linux o
Windows”
import platform
platform.uname()
# """
sistema_operativo = platform.system()
version = platform.version()
plataforma = platform.platform()
arquitectura = platform.architecture()
machine = platform.machine()
procesador = platform.processor()

print(sistema_operativo)
print(version)
print(plataforma)
print(arquitectura)
print(machine)
print(procesador)

"""
Problema 4:
Realizar una función que reciba un directorio y muestre todos los archivos y
carpetas que posee. Del resultado, de la lista anterior, realice una función que:
a)que diga si es o no un archivo de python.
b)cuente la cantidad total de archivos de python que hay en el directorio
"""


def listar_directorios(folder):
    lista_directorios = os.listdir(folder)
    identifica_archivo(lista_directorios)


def identifica_archivo(lista):
    cantidad = 0
    for archivo in lista:
        if archivo.__contains__('.py'):
            cantidad += 1
            print(archivo)
    print(f'Hay {cantidad} archivos de python')

listar_directorios(os.getcwd())
