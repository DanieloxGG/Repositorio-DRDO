# 40b: Versión alternativa que he decidido hacer yo, donde se introduce el valor del número máximo.

n=int(input("Introduce el número máximo: "))
pares=0
impares=0
indice=0

for i in range(0,n):
    indice=indice+1
    if indice/2 == round(indice/2):
        pares=pares+1
    else:
        impares=impares+1

print(f"Hay {pares} números pares.")
print(f"Hay {impares} números impares.")