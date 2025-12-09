# 60:  Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
# Utiliza únicamente el while.

num=int(input("Introduce un número: "))
indice=1
print("")

while indice <= 10:
    print(f"{num*indice}")
    indice=indice+1

print("")
