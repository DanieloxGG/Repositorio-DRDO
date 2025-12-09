# 64: Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
# -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
# a) total de pares
# b) total de impares
# c) total de números positivos
# d) total de números negativos
# e) total de ceros
# f) total de la suma de todos los números introducidos

num=0
par=0
impar=0
pos=0
neg=0
suma=0
print("Introduce el '-99' para finalizar el programa.")
while not num == -99:
    num=int(input("Introduce un número: "))
    if num % 2 == 0:
        par=par+1
    else:
        impar=impar+1
    if num >= 0:
        pos=pos+1
    else:
        neg=neg+1
    if not num == -99:
        suma=suma+num

print("")
print("RESUMEN:")
print(f"El número de pares es {par}")
print(f"El número de impares es {impar}")
print(f"El número de positivos es {pos}")
print(f"El número de negativos es {neg}")
print(f"La suma total es de {suma}")
