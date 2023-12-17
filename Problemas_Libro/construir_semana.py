#Construir un algoritmo que escriba los nombres de los días de la semana, en función de la entrada correspondiente
#a la variable DIA.

dia = int(input("Dia: "))
if dia == 1:
    print("Lunes.")
elif dia == 2:
    print("Martes.")
elif dia == 3:
    print("Miercoles.")
elif dia == 4:
    print("Jueves.")
elif dia == 5:
    print("Viernes.")
elif dia == 6:
    print("Sabado.")
elif dia == 7:
    print("Domingo.")
else:
    print("Escribe un numero del 1 al 7.")