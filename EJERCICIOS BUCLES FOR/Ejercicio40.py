# 40: Crea un programa que cuente todos los números pares hasta el número 50

pares=0
impares=0
indice=0

for i in range(0,50):
    indice=indice+1
    if indice/2 == round(indice/2):
        pares=pares+1
    else:
        impares=impares+1

print(f"Hay {pares} números pares.")
print(f"Hay {impares} números impares.")
