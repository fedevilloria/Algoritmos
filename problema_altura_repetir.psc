Algoritmo problema_altura_repetir
	definir cantidad_personas, dni, dni_persona_mayor Como Entero;
	definir altura, altura_maxima, decision Como Real;
	definir nombre, apellido, nombre_persona_mayor, apellido_persona_mayor Como Caracter;
	decision <- 1;
	altura_maxima <- 0;
	dni_persona_mayor <- 0;
	
	//Entrada
	Escribir "Que desea realizar?";
	Escribir "1) Ingresar datos de la persona al sistema.";
	Escribir "0) Cerrar programa.";
	Leer decision;
	
	Repetir
		Escribir "Ingrese su D.N.I.: ";
		Leer dni;
		Escribir "Ingrese su nombre: ";
		Leer nombre;
		Escribir "Ingrese su apellido: ";
		Leer apellido;
		Escribir "Ingrese su altura: ";
		Leer altura;
		
		//Proceso
		Si altura_maxima <= altura Entonces
			altura_maxima <- altura;
			dni_persona_mayor <- dni;
			nombre_persona_mayor <- nombre;
			apellido_persona_mayor <- apellido;
		FinSi
		
		Escribir "-----------------------------";
		Escribir "Seleccione que desea hacer:";
		Escribir "1) Seguir cargando datos.";
		Escribir "0) Finalizar recuento.";
		Leer decision;
		Escribir "-----------------------------";
	Hasta Que decision <> 1;
	
	//Salida
	Escribir "El alumno ", nombre_persona_mayor, " ", apellido_persona_mayor, " ", "con D.N.I. numero: ", dni_persona_mayor, " es la persona mas alta con ", altura_maxima, " metros.";
	
FinAlgoritmo