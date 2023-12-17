Proceso PuntoDeSilla
	Definir MatrizA Como Entero;
	Definir i, filas Como Entero;
	Definir j, columnas Como Entero;
	Definir num Como Entero;
	Definir maximo_fila, minimo_columna, maximo_columna, minimo_fila Como Entero;
	Definir contador, auxiliar Como Entero;
	Definir punto_silla Como Entero;
	
	Dimension MatrizA[100,100];
	Dimension maximo_fila[100];
	Dimension minimo_columna[100];
	Dimension maximo_columna[100];
	Dimension minimo_fila[100];
	Dimension punto_silla[100];
	
	maximo_fila[1] <- -999;
	maximo_fila[2] <- -999;
	maximo_fila[3] <- -999;
	maximo_fila[4] <- -999;
	maximo_fila[5] <- -999;
	maximo_fila[6] <- -999;
	maximo_fila[7] <- -999;
	maximo_fila[8] <- -999;
	
	minimo_columna[1] <- 999;
	minimo_columna[2] <- 999;
	minimo_columna[3] <- 999;
	minimo_columna[4] <- 999;
	minimo_columna[5] <- 999;
	minimo_columna[6] <- 999;
	minimo_columna[7] <- 999;
	minimo_columna[8] <- 999;
	
	maximo_columna[1] <- -999;
	maximo_columna[2] <- -999;
	maximo_columna[3] <- -999;
	maximo_columna[4] <- -999;
	maximo_columna[5] <- -999;
	maximo_columna[6] <- -999;
	maximo_columna[7] <- -999;
	maximo_columna[8] <- -999;
	
	minimo_fila[1] <- 999;
	minimo_fila[2] <- 999;
	minimo_fila[3] <- 999;
	minimo_fila[4] <- 999;
	minimo_fila[5] <- 999;
	minimo_fila[6] <- 999;
	minimo_fila[7] <- 999;
	minimo_fila[8] <- 999;
	
	contador <- 0;
	Para i<-1 Hasta 90 Hacer
		punto_silla[i] <- -1;
	FinPara
	
	Leer filas;
	Leer columnas;

	Mientras filas <> 0 & columnas <> 0 Hacer
		//Cargar la matriz e imprimirla
		Para i<-1 Hasta filas Hacer
			Para j<-1 Hasta columnas Hacer
				Leer MatrizA[i,j];
			FinPara
		FinPara
		
		//Maximo de fila y minimo de columna
		Para i<-1 Hasta filas Hacer
			Para j<-1 Hasta columnas Hacer
				Si MatrizA[i,j] > maximo_fila[i] Entonces
					maximo_fila[i] <- MatrizA[i,j];
				FinSi
				Si MatrizA[i,j] < minimo_columna[j] Entonces
					minimo_columna[j] <- MatrizA[i,j];
				FinSi
			FinPara
		FinPara
		
		Para i<-1 Hasta filas Hacer
			Para j<-1 Hasta columnas Hacer
				Si MatrizA[i,j] > maximo_columna[j] Entonces
					maximo_columna[j] <- MatrizA[i,j];
				FinSi
				Si MatrizA[i,j] < minimo_fila[i] Entonces
					minimo_fila[i] <- MatrizA[i,j];
				FinSi
			FinPara
		FinPara
		
		Para i<-1 Hasta filas Hacer
			Para j<-1 Hasta columnas Hacer
				Si maximo_fila[i] = minimo_columna[j] o maximo_columna[j] = minimo_fila[i] Entonces
					punto_silla[contador] <- 1;
				SiNo
					punto_silla[contador] <- 0;
				FinSi
			FinPara
		FinPara
		
		maximo_fila[1] <- -999;
		maximo_fila[2] <- -999;
		maximo_fila[3] <- -999;
		maximo_fila[4] <- -999;
		maximo_fila[5] <- -999;
		maximo_fila[6] <- -999;
		maximo_fila[7] <- -999;
		maximo_fila[8] <- -999;
		
		minimo_columna[1] <- 999;
		minimo_columna[2] <- 999;
		minimo_columna[3] <- 999;
		minimo_columna[4] <- 999;
		minimo_columna[5] <- 999;
		minimo_columna[6] <- 999;
		minimo_columna[7] <- 999;
		minimo_columna[8] <- 999;
		
		maximo_columna[1] <- -999;
		maximo_columna[2] <- -999;
		maximo_columna[3] <- -999;
		maximo_columna[4] <- -999;
		maximo_columna[5] <- -999;
		maximo_columna[6] <- -999;
		maximo_columna[7] <- -999;
		maximo_columna[8] <- -999;
		
		minimo_fila[1] <- 999;
		minimo_fila[2] <- 999;
		minimo_fila[3] <- 999;
		minimo_fila[4] <- 999;
		minimo_fila[5] <- 999;
		minimo_fila[6] <- 999;
		minimo_fila[7] <- 999;
		minimo_fila[8] <- 999;
		contador <- contador + 1;
		
		Leer filas;
		Leer columnas;
		
	FinMientras
	
	Para i<-1 Hasta punto_silla[i] Hacer
		Si punto_silla[i] = 1 Entonces
			Escribir "SI";
		FinSi
		Si punto_silla[i] = 0 Entonces
			Escribir "NO";
		FinSi
	FinPara

	
FinProceso
