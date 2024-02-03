Algoritmo matriz10x10
	//Villoria, Federico Martin - Legajo: 13906.
	
	Definir matriz, i, j Como Entero;
	Definir numero_mayor1, numero_menor1 Como Entero;
	Definir numero_mayor2, numero_menor2 Como Entero;
	Definir numero_mayor3, numero_menor3 Como Entero;
	Definir numero_mayor4, numero_menor4 Como Entero;
	Definir fila_mayor1, columna_mayor1, fila_menor1, columna_menor1 Como Entero;
	Definir fila_mayor2, columna_mayor2, fila_menor2, columna_menor2 Como Entero;
	Definir fila_mayor3, columna_mayor3, fila_menor3, columna_menor3 Como Entero;
	Definir fila_mayor4, columna_mayor4, fila_menor4, columna_menor4 Como Entero;
	
	Dimension matriz[11,11];
	
	Para i<-1 Hasta 10 Hacer
		Para j<-1 Hasta 10 Hacer
			matriz[i,j] <- azar(100);
		FinPara
	FinPara
	
	Para i<-1 Hasta 10 Hacer
		Escribir " ";
		Para j<-1 Hasta 10 Hacer
			Escribir Sin Saltar matriz[i,j], " ";
		FinPara
	FinPara
	
	Escribir " ";
	
	//Recorrer la primer parte de la matriz
	numero_mayor1 <- 0;
	numero_menor1 <- 100;
	Para i<-1 Hasta 5 Hacer
		Para j<-1 Hasta 5 Hacer
			Si matriz[i,j] > numero_mayor1 Entonces
				numero_mayor1 <- matriz[i,j];
				fila_mayor1<-i;
				columna_mayor1<-j;
			FinSi
			Si matriz[i,j] < numero_menor1 Entonces
				numero_menor1 <- matriz[i,j];
				fila_menor1 <- i;
				columna_menor1 <- j;
			FinSi
		FinPara
	FinPara
	Escribir " ";
	Escribir "--------------------------------------------";
	Escribir " ";
	Escribir "Primera zona de la matriz:";
	Escribir "El numero mayor es: ", numero_mayor1, " en la posicion (",fila_mayor1,",",columna_mayor1,")";
	Escribir "El numero menor es: ", numero_menor1, " en la posicion (",fila_menor1,",",columna_menor1,")";
	
	//Recorrer la segunda parte de la matriz
	numero_mayor2 <- 0;
	numero_menor2 <- 100;
	Para i<-1 Hasta 5 Hacer
		Para j<-6 Hasta 10 Hacer
			Si matriz[i,j] > numero_mayor2 Entonces
				numero_mayor2 <- matriz[i,j];
				fila_mayor2<-i;
				columna_mayor2<-j;
			FinSi
			Si matriz[i,j] < numero_menor2 Entonces
				numero_menor2 <- matriz[i,j];
				fila_menor2 <- i;
				columna_menor2 <- j;
			FinSi
		FinPara
	FinPara
	Escribir " ";
	Escribir "--------------------------------------------";
	Escribir " ";
	Escribir "Segunda zona de la matriz:";
	Escribir "El numero mayor es: ", numero_mayor2, " en la posicion (",fila_mayor2,",",columna_mayor2,")";
	Escribir "El numero menor es: ", numero_menor2, " en la posicion (",fila_menor2,",",columna_menor2,")";
	
	//Recorrer la tercera parte de la matriz
	numero_mayor3 <- 0;
	numero_menor3 <- 100;
	Para i<-6 Hasta 10 Hacer
		Para j<-1 Hasta 5 Hacer
			Si matriz[i,j] > numero_mayor3 Entonces
				numero_mayor3 <- matriz[i,j];
				fila_mayor3<-i;
				columna_mayor3<-j;
			FinSi
			Si matriz[i,j] < numero_menor3 Entonces
				numero_menor3 <- matriz[i,j];
				fila_menor3 <- i;
				columna_menor3 <- j;
			FinSi
		FinPara
	FinPara
	Escribir " ";
	Escribir "--------------------------------------------";
	Escribir " ";
	Escribir "Tercera zona de la matriz:";
	Escribir "El numero mayor es: ", numero_mayor3, " en la posicion (",fila_mayor3,",",columna_mayor3,")";
	Escribir "El numero menor es: ", numero_menor3, " en la posicion (",fila_menor3,",",columna_menor3,")";
	
	//Recorrer la cuarta parte de la matriz
	numero_mayor4 <- 0;
	numero_menor4 <- 100;
	Para i<-6 Hasta 10 Hacer
		Para j<-6 Hasta 10 Hacer
			Si matriz[i,j] > numero_mayor4 Entonces
				numero_mayor4 <- matriz[i,j];
				fila_mayor4<-i;
				columna_mayor4<-j;
			FinSi
			Si matriz[i,j] < numero_menor4 Entonces
				numero_menor4 <- matriz[i,j];
				fila_menor4 <- i;
				columna_menor4 <- j;
			FinSi
		FinPara
	FinPara
	Escribir " ";
	Escribir "--------------------------------------------";
	Escribir " ";
	Escribir "Cuarta zona de la matriz:";
	Escribir "El numero mayor es: ", numero_mayor4, " en la posicion (",fila_mayor4,",",columna_mayor4,")";
	Escribir "El numero menor es: ", numero_menor4, " en la posicion (",fila_menor4,",",columna_menor4,")";
FinAlgoritmo