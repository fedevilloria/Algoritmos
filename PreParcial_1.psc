Proceso PreParcial_1
	Definir MatrizA, filas, columnas, num Como Entero;
	Definir i, j Como Entero;
	Definir contador_pares Como Entero;
	
	Dimension MatrizA[100,100];
	
	Escribir "Ingrese la cantidad de filas que desea: ";
	Leer filas;
	
	Escribir "Ingrese la cantidad de columnas que desea: ";
	Leer columnas;
	
	//Cargar la matriz
	Para i<-1 Hasta filas Hacer
		Para j<-1 Hasta columnas Hacer
			Escribir "Ingrese el numero para la posicion ", i, ", ", j;
			Leer num;
			Si num = 0 o num = 1 Entonces
				MatrizA[i,j] <- num;
			SiNo
				Escribir "Por favor ingrese 0 o 1";
				Leer num;
				MatrizA[i,j] <- num;
			FinSi
		FinPara
	FinPara
	
	//Imprimir la matriz
	Para i<-1 Hasta filas Hacer
		Escribir " ";
		Para j<-1 Hasta columnas Hacer
			Escribir Sin Saltar MatrizA[i,j], " ";
		FinPara
	FinPara
	Escribir " ";
	
	//Contar la cantidad de 1 por fila
	contador_pares <- 0;
	Para i<-1 Hasta filas Hacer
		Para j<-1 Hasta columnas Hacer
			Si MatrizA[i,j] = 1 Entonces
				contador_pares <- contador_pares + 1;
			FinSi
			Si contador_pares Mod 2 = 0 Entonces
				MatrizA[i,columnas + 1] <- 0;
			SiNo
				MatrizA[i,columnas + 1] <- 1;
			FinSi
		FinPara
	FinPara
	
	//Imprimir la matriz
	Para i<-1 Hasta filas Hacer
		Escribir " ";
		Para j<-1 Hasta 4 Hacer
			Escribir Sin Saltar MatrizA[i,j], " ";
		FinPara
	FinPara
	Escribir " ";
	
FinProceso
