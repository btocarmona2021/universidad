# Ejercicio 2:
# a) cree una lista con los 4 nombres de usuarios del sistema “xxxx”
# b) muestre todos los nombres de usuarios.
# c) cree una nueva lista con: la lista ordenada, la lista invertida (del último al primero), los dos
# últimos elementos, los dos primeros elementos
# d) agregue un usuario más, y que ese nombre lo ingrese desde el teclado
# e) arme una función que le permita agregar usuarios a su lista.
# f) arme una función que le permita buscar un usuario en su lista.

def agregar_usuario(lista):
    nuevo = input("Ingrese el nombre del nuevo usuario-> ")
    lista.append(nuevo)


def buscar_usuario(lista_usuarios):
    usuario_buscado = input("Ingrese el nombre de usuario que busca-> ")
    if usuario_buscado in lista_usuarios:
        print(f"El usuario {usuario_buscado} se encuentra en la lista")
    else:
        print(f"Lo siento el usuario {usuario_buscado} no se encuentra en la lista")


print("Ejercicio A")
usuarios_sistema = ["Fabian", "Daniela", "Natalia", "julio"]

print("Ejercicio B")
for usuario in usuarios_sistema:
    print(usuario)

print("Ejercicio C")
usuarios_sistema.sort()
usuarios_sistema.reverse()

print("Ejercicio D")
nuevo_usuario = input("Ingrese el nombre del nuevo usuario-> ")
usuarios_sistema.append(nuevo_usuario)

print("Ejercicio E")
agregar_usuario(usuarios_sistema)

print("Ejercicio F")
buscar_usuario(usuarios_sistema)




