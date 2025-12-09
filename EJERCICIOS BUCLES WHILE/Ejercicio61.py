# 61: A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
# superior o igual a 40.

num=int(input("Introduce un número: "))
indice=1
print("")

while indice <= 10 and num*indice < 40:
    print(f"{num*indice}")
    indice=indice+1

print(f"{num*indice}")
print("Fin del programa.")
print("")