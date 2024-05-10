"""
Ejercicio 7

Sin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x= 6,
y=7. Practicar con traza.
def coordenadaZ(x,y):
x=x+10
y=y+15
return x+y
#principal
x=int(input(“Coordenada eje x: “))
x=int(input(“Coordenada eje y: “))
for i in range(3)
z=coordenadaZ(x,y)
x=x+1
y=y+1
print(X,” . “,y)

"""


# La salida estimo seria valor 9 para x y 10 para y ya que inician en 6 y 7 y luego en un bucle repetitivo
# de 3 iteraciones se incrementa en uno en cada iteracion.

def coordenada_z(x, y):
    x = x + 10
    y = y + 15
    return x + y


# principal
x = int(input("Coordenada eje x: "))

y = int(input("Coordenada eje y: "))

for i in range(3):
    z = coordenada_z(x, y)
    x = x + 1
    y = y + 1

print(x, ".", y)
