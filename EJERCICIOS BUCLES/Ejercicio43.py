# 43:  Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
# por pantalla cada letra.

palabra=input("Introduce una palabra: ")

indice=0

for i in range(0,len(palabra)):
    indice=indice+1
    print(f"La letra en la posición {indice} es {palabra[indice-1]}.")

