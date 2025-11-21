# 44b: Versión alternativa que he decidido hacer yo, donde se introduce el valor del número máximo.

nmax=int(input("Introduce el número máximo: "))
indice=0
num=0

for i in range(0,round(nmax/3)):
    indice=indice+1
    num=str(num)+","+str(indice*3)
print(f"{num}")