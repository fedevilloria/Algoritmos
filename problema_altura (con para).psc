Algoritmo problema_altura
	//Saber quien, cuantos y que cantidad de estudiantes fueron evaluados para obtener, el alumno mas alto de la comision, segun la cantidad de personas que la componen, en forma quincenal, porque cada 15 dias se renuevan las becas.
	
	//estas lineas representan la definicion de las variables que se utilizan en el pseudocodigo
	//variable es un espacio en memoria donde se almacena un dato el cual debe pertenecer a un tipo de dato

	definir cantidad_personas, dni, dni_persona_mayor, i, ContadorTotal Como Entero;
	definir altura, altura_maxima Como Real;
	definir nombre, apellido, nombre_persona_mayor, apellido_persona_mayor Como Caracter;
	
	//Entrada
	Escribir "Ingrese la cantidad total de personas en su comision: "; //Escribir permite mostrar valores por pantalla.
	Leer cantidad_personas; //Leer permite ingresar informacion desde el ambiente.
	//Toma N valores desde el ambiente por teclado y los asigna a la variable mencionada.
	
	Para i<-1 Hasta cantidad_personas Hacer //El Para ejecuta una secuencia de instrucciones un numero determinado de veces.
		Escribir "Ingrese su D.N.I.: ";
		Leer dni;
		Escribir "Ingrese su nombre: ";
		Leer nombre;
		Escribir "Ingrese su apellido: ";
		Leer apellido;
		Escribir "Ingrese su altura: ";
		Leer altura;
		//Proceso
		altura_maxima <- 0; //Asignacion o inicializacion de variables esta accion permite almacenar un valor en una variable.
		dni_persona_mayor <- 0;
		
		Si altura_maxima <= altura Entonces //Esta secuencia de instrucciones depende del valor de una condicion logica.
			//Se evalua dicha condicion y se ejecutan las instrucciones que correspondan.
			altura_maxima <- altura;
			dni_persona_mayor <- dni;
			nombre_persona_mayor <- nombre;
			apellido_persona_mayor <- apellido;
		FinSi
		ContadorTotal <- ContadorTotal + 1; //lo que hace el ContadorTotal es ir sumando constantemente 1 por cada usuario que ingresa.
	FinPara
	Escribir "participaron ", ContadorTotal, " personas";
	Escribir "El mas alto de la comision es ", nombre_persona_mayor, " ", apellido_persona_mayor, " su numero de D.N.I. es: ", dni_persona_mayor, " y su altura es ", altura_maxima, " metros.";
	FinAlgoritmo