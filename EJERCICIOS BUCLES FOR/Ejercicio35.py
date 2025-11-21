# 35: Programa que al introducir un número por teclado permita mostrar ese número de veces tu 
# nombre.

nom=input("Introduce tu nombre: ")
num=int(input("Introduce el número de veces: "))

print("")

# El "range(0,x)"" establece cuantas veces se repite lo que hay dentro del bucle.

for int in range(0,num):
    print(f"{nom}")