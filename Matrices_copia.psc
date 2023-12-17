Proceso Matrices_copia
	Definir MatrizA, i, j, num Como Entero;
	Definir filausuario, columnausuario Como Entero;
	Definir numeroingresado Como Entero;
	Definir sumatotal, sumafila, sumacolumna Como Entero;
	Definir numero_mayor, indice_mayor_fila, indice_mayor_columna Como Entero;
	Definir numero_menor, indice_menor_fila, indice_menor_columna Como Entero;
	Definir sumatoria_pares, sumatoria_impares Como Entero;
	
	Dimension MatrizA[100,100];
	
	//Cargar una Matriz cuya cantidad de elementos son definidas por el usuario (check)
	//Escribir la matriz ingresada (check)
	//Asignar un valor determinado en una posicion determinada (check)
	//Sumar todos los elementos de la Matriz (check)
	//Sumar los elementos que componen cada fila de la Matriz (check)
	//Sumar los elementos que componen cada columna de la Matriz (check)
	//Obtener el mayor elemento de la matriz conjuntamente con su posicion (check)
	//Obtener el menor elemento de la matriz conjuntamente con su posicion (check)
	//Obtener de las posiciones pares la sumatoria y el contenido de cada una (check)
	//Obtener de las posiciones impares la sumatoria y el contenido de cada una (check)
	//Escribir todos los resultados solicitados (check)
	
	//Cargar una matriz
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			Escribir "Ingrese el número para la posicion: ", i,", ", j;
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
	
	Escribir " ";
	Escribir " ";
	
	//Asignar un valor a una posicion determinada
	Escribir "Ingrese el número de fila donde desea cargar el numero: ";
	Leer filausuario;
	Escribir "Ingrese el número de columna donde desea cargar el numero: ";
	Leer columnausuario;
	Escribir "Ingrese el número que desea ingresar en la matriz: ";
	Leer numeroingresado;
	MatrizA[filausuario,columnausuario] <- numeroingresado;
	
	Para i<-1 Hasta 5 Hacer
		Escribir " ";
		Para j<-1 Hasta 5 Hacer
			Escribir Sin Saltar MatrizA[i,j], " ";
		FinPara
	FinPara
	
	Escribir " ";
	Escribir " ";
	
	//Suma total de la Matriz
	sumatotal <- 0;
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			sumatotal <- sumatotal + MatrizA[i,j];
		FinPara
	FinPara
	
	Escribir "Suma total: ", sumatotal;
	
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
				indice_mayor_fila <- i;
				indice_mayor_columna <- j;
			FinSi
		FinPara
	FinPara
	Escribir "El numero mayor de su matriz es: ", numero_mayor, " y su posición es [",indice_mayor_fila,",", indice_mayor_columna,"]",;	
	
	//Recorrer la matriz y obtener el menor
	numero_menor <- numero_mayor;
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			Si MatrizA[i,j] < numero_menor Entonces
				numero_menor <- MatrizA[i,j];
				indice_menor_fila <- i;
				indice_menor_columna <- j;
			FinSi
		FinPara
	FinPara
	Escribir "El numero mayor de su matriz es: ", numero_menor, " y su posición es [",indice_menor_fila,",", indice_menor_columna,"]",;
	
	Escribir " ";
	
	//Obtener de las posiciones pares la sumatoria y el contenido de cada una
	sumatoria_pares <- 0;
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			Si i Mod 2 = 0 y j Mod 2 = 0 Entonces
				sumatoria_pares <- sumatoria_pares + MatrizA[i,j];
				Escribir Sin Saltar MatrizA[i,j], " ";
			FinSi
		FinPara
	FinPara
	Escribir " ";
	Escribir "La sumatoria de los elementos que tengan índice par es: ", sumatoria_pares;
	
	Escribir " ";
	
	//Obtener de las posiciones impares la sumatoria y el contenido de cada una
	sumatoria_impares <- 0;
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			Si i Mod 2 <> 0 y j Mod 2 <> 0 Entonces
				sumatoria_impares <- sumatoria_impares + MatrizA[i,j];
				Escribir Sin Saltar MatrizA[i,j], " ";
			FinSi
		FinPara
	FinPara
	Escribir " ";
	Escribir "La sumatoria de los elementos que tengan índice impar es: ", sumatoria_impares;
	
FinProceso
