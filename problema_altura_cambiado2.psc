Algoritmo problema_altura2
	definir cantidad_personas, dni, dni_persona_mayor, decision, contador, contador_persona_mayor Como Entero;
	definir altura, altura_maxima Como Real;
	definir nombre, apellido, nombre_persona_mayor, apellido_persona_mayor Como Caracter;
	decision <- 1;
	altura_maxima <- 0;
	dni_persona_mayor <- 0;
	contador <- 0;
	
	//Entrada
	Escribir "Que desea realizar?";
	Escribir "1) Ingresar datos de la persona al sistema.";
	Escribir "0) Cerrar programa.";
	Leer decision;
	
	Si decision = 1 Entonces
		Mientras decision <> 0 Hacer
			Escribir "Ingrese su D.N.I.: ";
			Leer dni;
			Escribir "Ingrese su nombre: ";
			Leer nombre;
			Escribir "Ingrese su apellido: ";
			Leer apellido;
			Escribir "Ingrese su altura: ";
			Leer altura;
			contador <- contador + 1; //Este contador se utiliza para llevar el recuento de las personas totales registradas.
			
			//Proceso
			Si altura_maxima < altura Entonces
				altura_maxima <- altura;
				dni_persona_mayor <- dni;
				nombre_persona_mayor <- nombre;
				apellido_persona_mayor <- apellido;
				contador_persona_mayor <- 1; //Se reinicia el contador cuando se encuentra una nueva altura maxima.
			SiNo
				Si altura_maxima = altura Entonces
					contador_persona_mayor <- contador_persona_mayor + 1; //El contador se incrementa cuando se encuentra otra persona con la misma altura.
					//Es un contador ya que la cantida que se suma o resta es constante.
					//Acumulador siempre suma o resta una cantidad variable. Ej: suma_dni = suma_dni + dni.
				FinSi
			FinSi
			
			Escribir "-----------------------------";
			Escribir "Seleccione que desea hacer:";
			Escribir "1) Seguir cargando datos.";
			Escribir "0) Finalizar recuento.";
			Leer decision;
			Escribir "-----------------------------";
		FinMientras
			
		Escribir "Se analizaron ", contador," alumnos.";
		Si contador_persona_mayor > 1 Entonces
			Escribir "Los mas altos de la comision son ", contador_persona_mayor," personas.";
			Escribir "El mas alto es: ", nombre_persona_mayor, " ", apellido_persona_mayor," con D.N.I. numero: ", dni_persona_mayor, " y una altura de ", altura_maxima, " metros.";
		SiNo
			Escribir "El mas alto es: ", nombre_persona_mayor, " ", apellido_persona_mayor," con D.N.I. numero: ", dni_persona_mayor, " y una altura de ", altura_maxima, " metros.";
		FinSi
		
	SiNo
		Escribir "No se han ingresado alumnos.";
	FinSi
	
FinAlgoritmo