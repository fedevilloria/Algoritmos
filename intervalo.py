#EJERCICIO C
#Debes hacer un programa que lea un número de punto flotante e imprimir un mensaje diciendo en cuál de los siguientes
#intervalos el número pertenece: [0,25] (25,50], (50,75], (75,100). Número es menor que cero o mayor que 100, el programa
#debe imprimir el mensaje "Fora de intervalo" que significa "Fuera de intervalo".

#El símbolo '(' representa mayor que, por ejemplo:
#[0,25] indica números entre 0 y 25.0000, incluyendo ambos.
#(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

numero = float(input())
if numero > 100 or numero < 0:
    print("Fora de intervalo")

elif numero >= 0 and numero <= 25:
    print("Intervalo [0,25]")
elif numero > 25 and numero <= 50:
    print("Intervalo (25,50]")
elif numero > 50 and numero <= 75:
    print("Intervalo (50,75]")
elif numero > 75 and numero <= 100:
    print("Intervalo (75,100]")