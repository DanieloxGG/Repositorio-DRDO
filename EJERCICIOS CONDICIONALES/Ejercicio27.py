# 27: Mejora el programa anterior para controlar que el valor introducido es una letra y en 
# caso de introducir un número, aparezca un aviso por pantalla.

print("")
letra=input("Introduce una letra, mayúscula o minúscula: ")
print("")

if letra.isupper():
    print(f"La letra {letra} está en mayúscula.")
if letra.islower():
    print(f"La letra {letra} está en minúscula.")
if letra.isnumeric():
    print(f"El valor introducido, {letra}, es un número.")
if not letra.islower() and not letra.isupper() and not letra.isnumeric():
    print(f"La letra {letra} está en ¿?")
print("")