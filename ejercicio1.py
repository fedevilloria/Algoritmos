#Escribir un programa solicite al usuario 100 valores enteros y los almacene en un vector.
#Posteriormente, debe calcular el valor máximo, mínimo y la media

valores = []
valor_maximo = 0
valor_minimo = 0
suma_numeros = 0
promedio = 0
for i in range(100):
    numero = int(input("Numero: "))
    indice = i + 1
    valores.append(numero)

for numero in valores:
    valor_maximo = max(valores)
    valor_minimo = min(valores)

for numero in valores:
    suma_numeros = suma_numeros + numero
    promedio = suma_numeros / len(valores)
    indice = numero + 1

print(f"El valor maximo es {valor_maximo} y su valor minimo es {valor_minimo}")
print(f"El promedio de todos sus numeros es: {promedio}")
