print("NUEVO PASSWORD, INSTRUCCIONES:")
print("")
print("1. La longitud de la password debe tener entre 6 y 8 carácteres.")
print("2. En cada posición se deben cumplir los siguientes requisitos.")
print("    Posición 1: Un número mayor o igual a 1 y menor o igual a 5.")
print("    Posición 2: Una letra minúscula.")
print("    Posición 3: Una letra mayúscula.")
print("    Posición 4: Uno de los siguientes símbolos: *; _ o @.")
print("    Posición 5: Una letra minúscula.")
print("    Posición 6: Un número mayor o igual a 6 y menor o igual a 9.")
print("    Posición 7: Uno de los siguientes símbolos: &; / o #.")
print("    Posición 8: Un número menor o igual a 5.")
print("")
c=input("Introduce la nueva password: ")
print("")

# Con esta variable controlaremos el número de errores.

errores=0

# Ahora se comprueban los requisitos.

if len(c) >= 6 and len(c) <= 8:
    if c[0].isnumeric():
        if not(int(c[0]) >= 1 and int(c[0]) <= 5):
            print("Error en el carácter 1.")
            errores=errores+1
    else:
        print("Error en el carácter 1.")
        errores=errores+1
    if not c[1].islower():
        print("Error en el carácter 2.")
        errores=errores+1
    if not c[2].isupper():
        print("Error en el carácter 3.")
        errores=errores+1
    if not(c[3] == "*" or c[3] == "_" or c[3] == "@"):
        print("Error en el carácter 4.")
        errores=errores+1
    if not c[4].islower():
        print("Error en el carácter 5.")
        errores=errores+1
    if c[5].isnumeric():
        if not(int(c[5]) >= 6 and int(c[5]) <= 9):
            print("Error en el carácter 6.")
            errores=errores+1
    else:
        print("Error en el carácter 6.")
        errores=errores+1
    if len(c) >= 7:
        if not(c[6] == "&" or c[6] == "/" or c[6] == "#"):
            print("Error en el carácter 7.")
            errores=errores+1
    if len(c) == 8:
        if c[7].isnumeric():
            if not int(c[7]) <= 5:
                print("Error en el carácter 8.")
                errores=errores+1
        else:
            print("Error en el carácter 8.")
            errores=errores+1


    if errores == 0:
        print(f"Contraseña válida, tu nueva contraseña es {c}")
        print("")
    else:
        print(f"Hay {errores} error/es en la contraseña {c}")
        print("")
        
else:
    print(f"Error, una longitud de {len(c)} carácteres en la contraseña no es válida.")