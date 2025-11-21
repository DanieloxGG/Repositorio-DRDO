# 56: Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
# compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
# dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
# visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
# realización de un pedido, si quiere gestionar otro. 
# El establecimiento contempla los siguientes descuentos:
# Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
# Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
# Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
# • El número de pedidos realizados
# • Total a pagar.
# • Total con IVA (10%)
# • Total con el descuento aplicado.

print("MENÚ: ")
print("1. Bocadillo de calamares - 9€")
print("2. Bocadillo de chistorra - 4.5€")
print("3. Bikini de jamón - 2.5€")
print("")
print("ACOMPAÑAMIENTOS: ")
print("1. Patatas finas - 1.5€")
print("2. Patatas gruesas - 1.75€")
print("3. Patatas rústicas - 2€")
print("")
print("BEBIDA: ")
print("1. Coca-Cola - 2€")
print("2. Acuarius - 1.5€")
print("3. Agua - 1€")
print("")

pedir=1
suma=0
pedidos=0

while pedir == 1:
    pedidos=pedidos+1
    boc=int(input("¿Qué bocadillo quieres?: "))
    aco=int(input("¿Qué acompañamiento quieres?: "))
    beb=int(input("¿Qué bebida quieres?: "))
    print("")
    if boc == 1:
        suma=suma+9
    elif boc == 2:
        suma=suma+4.5
    elif boc == 3:
        suma=suma+2.5
    else:
        print("Ese bocadillo no es válido.")
    if aco == 1:
        suma+suma+1.5
    elif aco == 2:
        suma=suma+1.75
    elif aco == 3:
        suma=suma+2
    else:
        print("Ese acompañamiento no es válido.")
    if beb == 1:
        suma=suma+2
    elif beb == 2:
        suma=suma+1.5
    elif beb == 3:
        suma=suma+1
    else:
        print("Esa bebida no es válida.")
    print("")

    pregunta=1
    while pregunta == 1:
        respuesta=input("¿Quieres seguir pidiendo? (S/N): ")
        respuesta=respuesta.lower()
        if respuesta == "s":
            print("")
            pregunta=0
        elif respuesta == "n":
            pedir=0
            pregunta=0
        else:
            print("Respuesta no válida.")
            print("")

if suma >= 20 and suma <= 30:
    desc=5
elif suma > 30:
    desc=15
else:
    desc=0

print("RESUMEN DEL PEDIDO:")
print("")
print(f"Has realizado {pedidos} pedidos.")
print(f"El total a pagar es de {suma}€.")
print(f"El total con IVA es {suma+(suma*10/100)}€.")
print(f"El total con un descuento de {desc}% es {suma-(suma*desc/100)}€.")