valores = []
cantidad_valores = int(input("Cantidad de numeros a ingresar: "))
for numero in range(cantidad_valores):
    valor_ingresado = int(input("Numero: "))
    suma_cien = valor_ingresado + 100
    valores.append(suma_cien)
print("Valores: ",valores)