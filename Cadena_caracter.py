#Ingresar una cadena de caracter
narrativa1 = str(input("Sr. Usuario, ingrese una cadena de caracter: "))
print(narrativa1)

narrativa2 = str(input("Sr. Usuario, ingrese una cadena de caracter: "))
print(narrativa2)

#Longitud de la cadena de caracter
longitud_narrativa1 = len(narrativa1)
longitud_narrativa2 = len(narrativa2)
print(f"La longitud de la cadena numero 1 es: {longitud_narrativa1} y de la segunda es: {longitud_narrativa2}")

#Subcadenas de caracteres
sub_cadena = narrativa1[0:10]
print(sub_cadena)

#Concatenar cadenas
union_cadenas = narrativa1 + narrativa2
print(union_cadenas)

#Pasar los caracteres a mayuscula
cadena_mayuscula = narrativa1.upper()
print(cadena_mayuscula)

#Pasar los caracteres a minuscula
cadena_minuscula = narrativa1.lower()
print(cadena_minuscula)

#Convertir a texto un numero
numero_ingresado = input("Ingrese un numero: ")
numero_ingresado = int(numero_ingresado)