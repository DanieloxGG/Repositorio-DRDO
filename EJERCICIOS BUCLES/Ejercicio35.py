# 35: Programa que al introducir un número por teclado permita mostrar ese número de veces tu 
# nombre.

nom=input("Introduce tu nombre: ")
num=int(input("Introduce el número de veces: "))

print("")

for int in range(1,num+1):
    print(f"{nom}")