valores = []
hola = []
for i in range(10):
    numero = int(input("numero: "))
    valores.append(numero)
print("Valores: ",valores)
valores = valores[::-1]
print(f"Valores invertidos: {valores}")
suma = 0
promedio = 0
for numero in valores:
    suma = suma + numero
    promedio = suma / len(valores)
print("Total: ",suma)
print("Promedio: ",promedio)
