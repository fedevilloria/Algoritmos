#EJERCICIO B
#Leer 4 valores enteros A, B, C y D. Luego, si B es mayor que C, D es mayor que A, la suma de C y D es mayor que la suma de A y B, C y D son valores
#positivos y A es par, escribir el mensaje “Valores aceitos” (Valores aceptados).
#De lo contrario, escriba el mensaje “Valores nao aceitos” (Valores no aceptados).
entrada = input()
valores = entrada.split()
a, b, c, d = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3])

if b > c and d > a and c+d > a+b and c > 0 and a%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")