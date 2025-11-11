# 48: Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
# esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
# tenga x oportunidades para ver si letra introducida está en esa palabra.

secreta=input("Introduce la palabra secreta: ")
secreta=secreta.lower()
print("")

# Simplemente comprobamos si la letra introducida está en la palabra.

for i in range(0,len(secreta)):
    letra=input("Adivina una letra: ")
    if secreta.__contains__(letra):
        print(f"La letra '{letra}' sí está en la palabra secreta.")
        print("")
    else:
        print(f"La letra '{letra}' no está en la palabra secreta.")
        print("")