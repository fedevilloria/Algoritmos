Algoritmo problema_altura
	//estas lineas representan la definicion de las variables que se utilizan en el pseudocodigo
	//variable es un espacio en memoria donde se almacena un dato el cual debe pertenecer a un tipo de dato
	
	definir verificacion, dni, dni_persona_mayor, i Como Entero;
	definir altura, altura_maxima Como Real;
	definir nombre, apellido, nombre_persona_mayor, apellido_persona_mayor Como Caracter;
	verificacion <- 1;
	altura_maxima <- 0;
	dni_persona_mayor <- 0;
	//Entrada
	
	//Toma N valores desde el ambiente por teclado y los asigna a la variable mencionada.
	
	Para i<-1 Hasta verificacion Hacer //El Para ejecuta una secuencia de instrucciones un numero determinado de veces.
		Escribir "Ingrese su D.N.I.: ";
		Leer dni;
		Escribir "Ingrese su nombre: ";
		Leer nombre;
		Escribir "Ingrese su apellido: ";
		Leer apellido;
		Escribir "Ingrese su altura: ";
		Leer altura;
		//Proceso
//Asignacion o inicializacion de variables esta accion permite almacenar un valor en una variable.
		
		
		Si altura_maxima <= altura Entonces //Esta secuencia de instrucciones depende del valor de una condicion logica.
			//Se evalua dicha condicion y se ejecutan las instrucciones que correspondan.
			altura_maxima <- altura;
			dni_persona_mayor <- dni;
			nombre_persona_mayor <- nombre;
			apellido_persona_mayor <- apellido;
		FinSi
		escribir "Ingrese por teclado uno de los siguientes valores:";
		escribir "(1): para continuar la carga de datos"; 
		escribir "(cualquier otro numero): para finalizar la carga de datos";
		leer verificacion;
		si verificacion = 1 Entonces
			i <- i - 1;
		FinSi
	FinPara
	Escribir "El mas alto de la comision es ", nombre_persona_mayor, " ", apellido_persona_mayor, " su numero de D.N.I. es: ", dni_persona_mayor, " y su altura es ", altura_maxima, " metros.";
FinAlgoritmo