#Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Se desea calcular el jornal diario de acuerdo con los siguientes puntos:
#1. la tarifa de las horas diurnas es de 5 euros,
#2. la tarifa de las horas nocturnas es de 8 euros,
#3. caso de ser domingo, la tarifa se incrementará en 2 euros el turno diurno y 3 euros el turno nocturno

tarifa_diurna = 5
tarifa_nocturna = 8
nombre = input("Nombre: ")
turno = input("Turno: ")
horas_trabajadas = int(input("Horas trabajadas: "))
dia_semana = input("Dia: ")

if turno == "Diurno" and dia_semana != "Domingo":
    tarifa_personal = tarifa_diurna * horas_trabajadas
    print(f"Hola {nombre}, por las horas trabajadas y ser {dia_semana} te corresponden ${tarifa_personal} euros.")
elif turno == "Diurno" and dia_semana == "Domingo":
    tarifa_personal = (tarifa_diurna + 2) * horas_trabajadas
    print(f"Hola {nombre}, por las horas trabajadas y ser {dia_semana} te corresponden ${tarifa_personal} euros.")
elif turno == "Nocturno" and dia_semana != "Domingo":
    tarifa_personal = tarifa_nocturna * horas_trabajadas
    print(f"Hola {nombre}, por las horas trabajadas y ser {dia_semana} te corresponden ${tarifa_personal} euros.")
else:
    tarifa_personal = (tarifa_nocturna + 3) * horas_trabajadas
    print(f"Hola {nombre}, por las horas trabajadas y ser {dia_semana} te corresponden ${tarifa_personal} euros.")