Proceso Matrices
	Definir MatrizA, i, j, num Como Entero;
	Definir filausuario, columnausuario Como Entero;
	Definir numeroingresado Como Entero;
	Definir sumatotal, sumafila, sumacolumna Como Entero;
	Definir numero_mayor Como Entero;
	
	Dimension MatrizA[100,100];
	
	//Cargar una Matriz cuya cantidad de elementos son definidas por el usuario (check)
	//Escribir la matriz ingresada (check)
	//Asignar un valor determinado en una posicion determinada (check)
	//Sumar todos los elementos de la Matriz (check)
	//Sumar los elementos que componen cada fila de la Matriz (check)
	//Sumar los elementos que componen cada columna de la Matriz (check)
	//Obtener el mayor elemento de la matriz conjuntamente con su posicion 
	//Obtener el menor elemento de la matriz conjuntamente con su posicion
	//Obtener de las posiciones pares la sumatoria y el contenido de cada una
	//Obtener de las posiciones impares la sumatoria y el contenido de cada una
	//Escribir todos los resultados solicitados
	
	//Cargar una matriz
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			Escribir "Ingrese el numero para la posicion: ", i,", ", j;
			Leer MatrizA[i,j];
		FinPara
	FinPara
	
	//Escribir la matriz ingresada
	Para i<-1 Hasta 5 Hacer
		Escribir " ";
		Para j<-1 Hasta 5 Hacer
			Escribir Sin Saltar MatrizA[i,j], " ";
		FinPara
	FinPara
	
	//Asignar un valor a una posicion determinada
	Escribir "Ingrese el numero de fila donde desea cargar el numero: ";
	Leer filausuario;
	Escribir "Ingrese el numero de columna donde desea cargar el numero: ";
	Leer columnausuario;
	Escribir "Ingrese el numero que desea ingresar en la matriz: ";
	Leer numeroingresado;
	MatrizA[filausuario,columnausuario] <- numeroingresado;
	
	Para i<-1 Hasta 5 Hacer
		Escribir " ";
		Para j<-1 Hasta 5 Hacer
			Escribir Sin Saltar MatrizA[i,j], " ";
		FinPara
	FinPara
	
	//Suma total de la Matriz
	Escribir " ";
	sumatotal <- 0;
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			sumatotal <- sumatotal + MatrizA[i,j];
		FinPara
	FinPara
	
	Escribir "Suma Total: ", sumatotal;
	
	//Suma total de todos los elementos de cada fila
	sumafila <- 0;
	Para j<-1 Hasta 5 Hacer
		sumafila <- sumafila + MatrizA[1,j];
	FinPara
	Escribir "La suma de la fila 1 es: ", sumafila;
	
	//Suma total de todos los elementos de cada columna
	sumacolumna <- 0;
	Para i<-1 Hasta 5 Hacer
		sumacolumna <- sumacolumna + MatrizA[i,1];
	FinPara
	Escribir "La suma de la columna 1 es: ", sumacolumna;
	
	//Recorrer la matriz y obtener el mayor
	numero_mayor <- 0;
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			Si MatrizA[i,j] > numero_mayor Entonces
				numero_mayor <- MatrizA[i,j];
			FinSi
		FinPara
	FinPara
	Escribir "El numero mayor de su matriz es: ", numero_mayor;
	
FinProceso
