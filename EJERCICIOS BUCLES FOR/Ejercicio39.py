# 39: Programa que pida n números y que, tras introducir el último número, debe aparecer por 
# pantalla el número total de positivos, negativos y número de 0.

n=int(input("Introduce el número de valores que quieres introducir: "))
print("")

pos=0
ceros=0
neg=0

for i in range(0,n):
    num=float(input("Introduce un número: "))
    if num > 0:
        pos=pos+1
    elif num == 0:
        ceros=ceros+1
    elif num < 0:
        neg=neg+1

print(f"Has introducido {pos} número(s) positivo(s), {neg} negativo(s) y {ceros} cero(s).")
