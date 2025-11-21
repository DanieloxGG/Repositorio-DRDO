# 45: Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
# distinguiendo vocales y las consonantes.

palabra=input("Introduce una palabra: ")
palabra=palabra.lower()
indice=0
vocpalabra=""
conpalabra=""

# Pongo vocales con acentos por si acaso.

vocales="aeiouáéíóúàèìòù"

for i in range(0,len(palabra)):
    if palabra[indice] in vocales:
        vocpalabra=vocpalabra+str(palabra[indice])
    else:
        conpalabra=conpalabra+str(palabra[indice])
    indice=indice+1

print(f"Las vocales en '{palabra}' son {vocpalabra}.")
print(f"Las consonantes en '{palabra}' son {conpalabra}.")