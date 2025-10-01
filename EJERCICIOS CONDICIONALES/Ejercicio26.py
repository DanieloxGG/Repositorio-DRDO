# 26: Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
# está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

print("")
letra=input("Introduce una letra, mayúscula o minúscula: ")
print("")

if letra.isupper():
    print(f"La letra {letra} está en mayúscula.")
if letra.islower():
    print(f"La letra {letra} está en minúscula.")
if not letra.islower() and not letra.isupper():
    print(f"El valor introducido no es una letra.")
print("")

