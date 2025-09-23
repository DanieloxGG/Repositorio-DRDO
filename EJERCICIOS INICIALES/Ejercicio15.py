# 15: Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
# introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math
rad=float(input("Escribe el radio del cilindro: "))
alt=float(input("Escribe la altura del cilindro: "))
print("")

area=round(2*math.pi*rad*(rad+alt), 2)
vol=round(math.pi*rad**2*alt, 2)

print(f"El área del cilindro es {area}.")
print(f"El volumen del cilindro es {vol}.")