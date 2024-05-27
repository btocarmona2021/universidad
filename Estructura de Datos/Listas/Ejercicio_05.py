# Ejercicio 5: Genere una lista con los N nombres usuarios habilitados para ingresar al sistema
# SIU, se los debe ingresar por teclado. Además se pide, armar otra lista llamada “ccaract” con
# la longitud de caracteres de cada nombre de usuario. Se desea saber en promedio cuál es la
# longitud de caracteres de los nombres de los
# usuarios

respuesta = ""
lista_usuarios = []
ccaract = []
ver_promedio = ""

while respuesta.lower() != "s":
    nombre = input("Ingrese el nombre de usuario del sistema Siu-> ")
    lista_usuarios.append(nombre)
    ccaract.append(len(nombre))
    ver_promedio = input("¿Desea ver el promedio de caracteres de los nombres de los usuarios? S/N-> ")
    suma_caracteres = 0
    if ver_promedio == "s":
        for cant in ccaract:
            suma_caracteres += cant
        print(f"El promedio de los caracteres de todos los nombres es {suma_caracteres / len(ccaract)} de un total de {len(ccaract)} alumnos"
              f" y de {suma_caracteres} caracteres")
    respuesta = input("Desea salir del sistema S/N-> ")
