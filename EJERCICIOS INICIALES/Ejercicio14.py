# 14: Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
# y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
# resultado a un decimal.
import math

diam=float(input("Introduce el diámetro del círculo: "))
print("")

rad=diam/2
per=diam*math.pi
area=math.pi*rad**2

print(f"El perímetro del círculo es {round(per, 1)}.")
print(f"El área del círculo es {round(area, 1)}.")

