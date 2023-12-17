#Leer dos numeros y deducir si estan en orden creciente
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))

if numero1 < numero2:
    print(f"Estan en orden creciente. {numero2}, {numero1}")
else:
    print("No estan en orden creciente.")