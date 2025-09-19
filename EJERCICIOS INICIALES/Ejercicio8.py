# 8: Programa que pida un número de horas y muestre por pantalla los minutos y segundos.

hor=float(input("Escribe un número de horas: "))
min=hor*60
seg=hor*3600
print("")

print(f"{hor} horas es igual a {min} minutos y {seg} segundos.")