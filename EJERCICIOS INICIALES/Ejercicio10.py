# 10:  Introduce por teclado dos números y muestre por pantalla la siguiente información: 
# cociente, resto y si el dividendo es par o impar.

import math

var1=float(input("Escribe el primer número: "))
var2=float(input("Escribe otro número: "))
print("")

print(f"El cociente es igual a {math.floor(var1/var2)}.")
print(f"El resto es igual a {var1%var2}")

if var1%2 == 0:
    print(f"El número {var1} es par.")
else:
    print(f"El número {var1} es impar.")
