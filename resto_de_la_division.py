#EJERCICIO D
#Escribir un programa que lea dos números enteros, X e Y. Imprimir todos
#los números entre X e Y que, dividiéndolo por 5, el resto sea igual a 2 o 3.

x = int(input())
y = int(input())

for numero in range(x, y):
    if numero % 5 == 2 or numero % 5 == 3:
        print(numero)