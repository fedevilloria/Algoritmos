#2
#Leer 4 valores enteros A, B, C y D. Luego, si B es mayor que C, D es mayor que A, la suma de C y D es mayor que la suma de A y B, C y D son valores positivos y A es par
# scribir el mensaje “Valores aceitos” (Valores aceptados). De lo contrario, escriba el mensaje “Valores nao aceitos” (Valores no aceptados).

#entrada = input()
#valores = entrada.split()
#a, b, c, d = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3])

#if b > c and d > a and c+d > a+b and c > 0 and a%2 == 0:
#    print("Valores aceitos")
#else:
#    print("Valores nao aceitos")

#3
#Debes hacer un programa que lea un número de punto flotante e imprimir un mensaje diciendo en cuál de los siguientes
# intervalos el número pertenece: [0,25] (25,50], (50,75], (75,100). Número es menor que cero o mayor que 100,
# el programa debe imprimir el mensaje "Fora de intervalo" que significa "Fuera de intervalo".
#El símbolo '(' representa mayor que, por ejemplo:
#[0,25] indica números entre 0 y 25.0000, incluyendo ambos.
#(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

#numero = float(input())
#if numero > 100 or numero < 0:
#    print("Fora de intervalo")

#elif numero >= 0 and numero <= 25:
#    print("Intervalo [0,25]")
#elif numero > 25 and numero <= 50:
#    print("Intervalo (25,50]")
#elif numero > 50 and numero <= 75:
#    print("Intervalo (50,75]")
#elif numero > 75 and numero <= 100:
#    print("Intervalo (75,100]")

#4
# Escribir un programa que lea dos números enteros, X e Y. Imprimir todos los números entre X e Y que,
# dividiéndolo por 5, el resto sea igual a 2 o 3.

x = int(input())
y = int(input())

for numero in range(x, y):
  if numero % 5 == 2 or numero % 5 == 3:
    print(numero)