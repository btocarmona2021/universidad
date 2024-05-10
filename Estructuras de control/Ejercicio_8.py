"""
Ejercicio 8: Héctor trabaja en una empresa de informática. En su computadora administra archivos de gran
tamaño y, por recomendación de su jefe, el archivo que trabajó en el día debe ser copiado en una carpeta
utilizando un software de la empresa. Este software le muestra a Héctor la cantidad de segundos que tardó en
realizar la copia. El problema es que Héctor necesita los “segundos” expresados en “minutos:segundos” para
elaborar un informe diario y no sabe cómo hacerlo. Por ejemplo:Ayer uno de los archivos tardó 513 segundos.
Antes de ayer otro archivo tardó 86 segundos. Programe el algoritmo que solucione el problema de Héctor
cada vez que lo necesite.
"""
import random
#Utilizo la libreria random y su metodo randint con la que genero un numero aleatorio entre 60 y 10000
segundos = random.randint(60, 10000)

#La funcion recibe los segundos generados y se encarga de convertirlo a minutos
# teniendo encuenta segundos sobrantes si los hubiera.
def calcula_minutos(segundos):
    min = int((segundos - segundos % 60) / 60)
    seg = segundos % 60
    return min, seg

#Recupero en dos variables lo retornado por la funcion, llamando a la misma
min, seg = calcula_minutos(segundos)

#Imprimo el resultado deseado por Héctor para ser presentado.
print("La tarea de Backup a demorado", segundos, "segundos lo que equivale a", min, "minutos con", seg, "segundos")
