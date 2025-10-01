# 28: Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
# elif.

# Practicamente el mismo código de antes, substituyendo los "if" por "elif".

print("")
letra=input("Introduce una letra, mayúscula o minúscula: ")
print("")

if letra.isupper():
    print(f"La letra {letra} está en mayúscula.")
elif letra.islower():
    print(f"La letra {letra} está en minúscula.")
elif letra.isnumeric():
    print(f"El valor introducido, {letra}, es un número.")
elif not letra.islower() and not letra.isupper() and not letra.isnumeric():
    print(f"El valor introducido,{letra} , es un símbolo.")
print("")