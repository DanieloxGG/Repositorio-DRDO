# 31: Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
# Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
# índice.

print("")
print("La frase es: A quien madruga Dios ayuda.")
frase="A quien madruga Dios ayuda."

palabra=input("Introduce una palabra, que esté en la frase o que no esté: ")
print("")

if frase.__contains__(palabra):
    print(f"La palabra {palabra} está en la frase, en el índice {frase.index(palabra)}.")
else:
    print(f"La palabra {palabra} no está en la frase.")

