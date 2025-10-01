# 30: Realiza un programa que controle si la longitud de una frase introducida por teclado es
# igual, menor o mayor de 11 caracteres. Utiliza elif.

print("")
frase=input("Introduce una frase: ")
print("")

if len(frase) == 11:
    print(f"La longitud de la frase es de 11 carácteres.")
elif len(frase) > 11:
    print(f"La longitud de la frase es mayor a 11 carácteres.")
else:
    print(f"La longitud de la frase es menor de 11 carácteres.")
print("")