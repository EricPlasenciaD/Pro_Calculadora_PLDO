
print ("\nElija dos numeros para realizar la operacion de sumar:")

try:
        num1 = float(input("introduzca un número: "))
        num2 = float(input("introduzca otro número: "))
except ValueError:
        print ("Introduzca un valor numérico")
        exit()
   
resultado = num1 + num2

print (f"el resultado de la operación es: {resultado}")


