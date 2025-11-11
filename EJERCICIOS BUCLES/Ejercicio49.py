# 49: A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
# indique en qué posición de la palabra se encuentra la letra.

secreta=input("Introduce la palabra secreta: ")
secreta=secreta.lower()
print("")

for i in range(0,len(secreta)):
    letra=input("Adivina una letra: ")
    if secreta.__contains__(letra):
        print(f"La letra '{letra}' sí está en la palabra secreta.")
        print(f"La letra está en la posición {secreta.index(letra)+1}")
        print("")
    else:
        print(f"La letra '{letra}' no está en la palabra secreta.")
        print("")