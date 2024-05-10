"""Ejercicio 4: Escriba una función que reciba la nota de un estudiante y devuelva la calificación en texto según la
siguiente configuración:
Nota = 10 → Excelente
Nota: 8 o 9 → Sobresaliente
Nota = 7 → Aprobado
Nota: 4 o 5 o 6 → Regular
Nota_ 1 o 2 o 3 → Desaprobado
El programa principal debe mostrar un mensaje donde se indique el Nombre del alumno, Materia y Calificación.
Por ejemplo:
“Alumno Jorge, su nota de Matemáticas es Sobresaliente”"""

nombre = input("Ingrese el nombre del estudiante-> ")
materia = input("Ingrese el nombre de la materia a calificar-> ")
nota = float(input("Ingrese la nota obtenida-> "))


def retorna_nota(nota):
    if nota == 10:
        return "genial", "Excelente"
    elif nota > 7 and nota < 10:
        return "muy bien,", "Sobresaliente"
    elif nota == 7:
        return "bien,lo has logrado,", "Aprobado"
    elif nota > 3 and nota < 7:
        return "bastante mejor,esfuerzate un poco mas,", "Regular"
    elif nota > 0 and nota < 4:
        return "flojo, debes esforzarte y practicar mas,", "Desaprobado"
    elif nota < 0 or nota > 10:
        return "La nota ingresada no esta en el rango de calificacion"


mensaje, resultado = retorna_nota(nota)

print("Hola ", nombre, "lo has realizado", mensaje, "tu nota en",materia,"ha sido", resultado)
