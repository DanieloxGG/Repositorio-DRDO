# 18: Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
# importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
# de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
# teclado el número de menores y el número de adultos que asisten al cine.

# Pongo el int por si a algún gracioso se le ocurre poner un número decimal de personas.

men=float(input("¿Cuantos menores de 18 años hay?: "))
may=float(input("¿Cuantos adultos hay?: "))
if round(may) == may and round(men) == men:
    print("")

    # El precio por menor será de 6 euros.
    # El precio por mayor será de 10.8 euros.

    precio=men*6+may*10.8

    print(f"El precio total a pagar es de {round(precio, 2)} €.")
else:
    print("Error, no puede haber un número decimal de personas.")



