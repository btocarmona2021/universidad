"""Ejercicio 5. Reciba como entrada el año de nacimiento de una persona y calcule aproximadamente su edad,
teniendo en cuenta solo su año de nacimiento y el año actual"""


# Funcion con la cual calculo la edad
def calcula_edad(anio):
    # return datetime.datetime.now().year - anio
    return 2024 - anio

#Solicito el año de nacimiento al usuario
anio_nacimiento = int(input("Por favor ingresa tu año de nacimiento: "))

#Llamo a la funcion la cual me devuelve la edad
print("Su edad es de: ", calcula_edad(anio_nacimiento))
