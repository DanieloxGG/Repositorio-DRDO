# 32. ¿Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
# no distinguir entre mayúsculas y minúsculas?

print("")
print("La frase es: A quien madruga Dios ayuda.")
frase="A quien madruga Dios ayuda."
# Transformamos la frase en todo minúsculas.
frase=frase.lower()
palabra=input("Introduce una palabra, que esté en la frase o que no esté: ")
# Transformamos la palabra introducida también en minúsculas.
palabra=palabra.lower()
print("")

if frase.__contains__(palabra):
    print(f"La palabra {palabra} está en la frase, en el índice {frase.index(palabra)}.")
else:
    print(f"La palabra {palabra} no está en la frase.")