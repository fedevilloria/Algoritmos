# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	narrativa1 = str()
	sub_cadena = str()
	narrativa2 = str()
	union = str()
	may = str()
	min = str()
	conversion_texto = str()
	long1 = int()
	long2 = int()
	conversion_numero = int()
	suma = int()
	print("Sr. Usuario, ingrese una cadena de caracter:")
	narrativa1 = input()
	print(narrativa1)
	print(" ")
	print("Sr. Usuario, ingrese una cadena de caracter:")
	narrativa2 = input()
	print(narrativa2)
	long1 = len(narrativa1)
	print(long1)
	long2 = len(narrativa2)
	print(long2)
	sub_cadena = narrativa1[0:11]
	print(sub_cadena)
	union = narrativa1+narrativa2
	print(union)
	may = str.upper(narrativa1)
	min = str.lower(narrativa1)
	print(may)
	print(min)
	conversion_numero = float(narrativa1)
	print(conversion_numero)
	suma = conversion_numero+1950
	print(suma)
	conversion_texto = str(suma)
	print(conversion_texto)

