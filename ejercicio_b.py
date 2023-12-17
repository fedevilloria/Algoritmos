#Leer la hora de inicio y final de un juego, en horas y minutos (hora inicial, minuto inicial, hora final, minuto final). 
#Luego mostrar la duración del juego, sabiendo que el juego puede comenzar en un día y terminar en el siguiente.
#Obs.: El tiempo máximo de juego es de 24 horas y el tiempo mínimo es de 1 minuto.
vector = []
cadena = str(input())
vector = cadena.split(' ')

hora_inicio = int(vector[0])
min_inicio = int(vector[1])
hora_final = int(vector[2])
min_final = int(vector[3])


if hora_inicio == hora_final and min_inicio == min_final:
    horas_totales = 24
    min_finales = 0
else:
    horas_i = hora_inicio * 60
    total_i = horas_i + min_inicio

    horas_f = hora_final * 60
    total_f = horas_f + min_final

    horas_totales = (total_f - total_i) // 60
    min_finales = ((total_f - total_i)/60 - horas_totales) * 60

    if horas_totales < 0:
        horas_totales = horas_totales + 24
    if min_finales < 0:
        min_finales = min_finales+ 60


print(f'O JOGO DUROU {horas_totales} HORA(S) E {round(min_finales)} MINUTO(S)')