# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	cantidad_personas = int()
	dni = int()
	dni_persona_mayor = int()
	decision = int()
	contador = int()
	contador_persona_mayor = int()
	altura = float()
	altura_maxima = float()
	nombre = str()
	apellido = str()
	nombre_persona_mayor = str()
	apellido_persona_mayor = str()
	decision = 1
	altura_maxima = 0
	dni_persona_mayor = 0
	contador = 0
	# Entrada
	print("Que desea realizar?")
	print("1) Ingresar datos de la persona al sistema.")
	print("0) Cerrar programa.")
	decision = int(input())
	if decision==1:
		while decision!=0:
			print("Ingrese su D.N.I.: ")
			dni = int(input())
			print("Ingrese su nombre: ")
			nombre = input()
			print("Ingrese su apellido: ")
			apellido = input()
			print("Ingrese su altura: ")
			altura = float(input())
			# Este contador se utiliza para llevar el recuento de las personas totales registradas.
			contador = contador+1
			# Proceso
			if altura_maxima<altura:
				altura_maxima = altura
				dni_persona_mayor = dni
				nombre_persona_mayor = nombre
				apellido_persona_mayor = apellido
				# Se reinicia el contador cuando se encuentra una nueva altura maxima.
				contador_persona_mayor = 1
			else:
				if altura_maxima==altura:
					# El contador se incrementa cuando se encuentra otra persona con la misma altura.
					contador_persona_mayor = contador_persona_mayor+1
					# Es un contador ya que la cantida que se suma o resta es constante.
					# Acumulador siempre suma o resta una cantidad variable. Ej: suma_dni = suma_dni + dni.
			print("-----------------------------")
			print("Seleccione que desea hacer:")
			print("1) Seguir cargando datos.")
			print("0) Finalizar recuento.")
			decision = int(input())
			print("-----------------------------")
		print("Se analizaron ",contador," alumnos.")
		if contador_persona_mayor>1:
			print("Los mas altos de la comision son ",contador_persona_mayor," personas.")
			print("El mas alto es: ",nombre_persona_mayor," ",apellido_persona_mayor," con D.N.I. numero: ",dni_persona_mayor," y una altura de ",altura_maxima," metros.")
		else:
			print("El mas alto es: ",nombre_persona_mayor," ",apellido_persona_mayor," con D.N.I. numero: ",dni_persona_mayor," y una altura de ",altura_maxima," metros.")
	else:
		print("No se han ingresado alumnos.")

