# 9:  Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos 
# y las horas.

seg=float(input("Escribe un número de segundos: "))
min=seg/60
hor=round(seg/3600, 2)
print("")

print(f"{seg} segundos es igual a {min} minutos y {hor} horas.")