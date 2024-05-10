def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


nro = int(input("Ingrese un numero: "))

if par(nro) == True:
    print("el numero es Par")
else:
    print("el numero es Impar")
