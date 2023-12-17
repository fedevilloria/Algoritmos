#Determinar el precio del billete de ida y vuelta en avión, conociendo la distancia a recorrer y sabiendo que si
#el número de días de estancia es superior a 7 y la distancia superior a 800 km el billete tiene una reducción del 30
#por 100. El precio por km es de 2,5 euros.

distancia_por_recorrer = float(input("Distancia a recorrer: "))
dias_estancia = float(input("Dias de estadia: "))

precio_total = distancia_por_recorrer*2.5
if distancia_por_recorrer > 800 and dias_estancia > 7:
    precio_descuento = (distancia_por_recorrer*2.5) - 30/100 * precio_total
    print(f"Su boleto le costaria ${precio_descuento} ARS")
else:
    print(f"Al no poder acceder al descuento el boleto le sale ${precio_total} ARS")