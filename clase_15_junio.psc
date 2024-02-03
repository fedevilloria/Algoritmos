Proceso clase_15_junio
	Definir A, numA, sumaA Como Caracter;
	Definir B, i, numB, sumaB Como Entero;
	
	Dimension A[100];
	Dimension B[100];
	
	//Lectura de Vector A
	Escribir "Vector A:";
	Para i<-1 Hasta 5 Hacer
		Leer numA;
		A[i] <- numA;
	FinPara
	
	Escribir " ";
	
	//Lectura de Vector B
	Escribir "Vector B:";
	Para i<-1 Hasta 5 Hacer
		Leer numB;
		B[i] <- numB;
	FinPara
	
	//Salida del Vector A
	Para i<-1 Hasta 5 Hacer
		Escribir Sin Saltar A[i], ", ";
	FinPara
	
	Escribir " ";
	
	//Salida del Vector B
	Para i<-1 Hasta 5 Hacer
		Escribir Sin Saltar B[i], ", ";
	FinPara
	
	Escribir " ";
	
	//Suma de los elementos del Vector A
	sumaA <- A[i];///??????????????????????????????
	Para i<-1 Hasta 5 Hacer
		sumaA <- Concatenar(sumaA,A[i]);
	FinPara
	Escribir "Suma de los elementos del vector A: ", sumaA ;
	
	//Suma de los elementos del Vector B
	sumaB <- 0;
	Para i<-1 Hasta 5 Hacer
		sumaB <- sumaB + B[i];
	FinPara
	Escribir "Suma de los elementos del vector B: ", sumaB;
	
FinProceso