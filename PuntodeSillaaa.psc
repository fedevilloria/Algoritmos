Proceso PuntodeSilla
	
	Definir MatrizA, i, j Como Entero;
	Definir filas, columnas Como Entero;
	Definir maximo_fila, minimo_columna Como Entero;
	
	Dimension MatrizA[100,100];
	Dimension maximo_fila[100];
	Dimension minimo_columna[100];
	
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
	
	Leer filas;
	Leer columnas;
	
	Mientras filas <> 0 y columnas <> 0 Hacer
		Para i<-1 hasta filas Hacer
			Para j<-1 hasta columnas Hacer
				Leer MatrizA[i,j];
			FinPara
		FinPara
		
		Leer filas;
		Leer columnas;
	FinMientras
	
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
	Escribir " ";
	Para i<-1 Hasta filas Hacer
		Para j<-1 Hasta columnas Hacer
			Si maximo_fila[i] = minimo_columna[j] Entonces
				Escribir "SI";
			FinSi
		FinPara
	FinPara
FinProceso
