# 65: Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
# -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.

num=0
mayor=0
menor=0

print("Introduce el '-99' para finalizar el programa.")
while not num == -99:
    num=int(input("Introduce un número: "))
    if not num == -99:
        if num > mayor:
            mayor=num
        if num < menor:
            menor=num
    

print("")
print("RESUMEN:")
print(f"El número más grande introducido es {mayor}")
print(f"El número más pequeño introducido es {menor}")

