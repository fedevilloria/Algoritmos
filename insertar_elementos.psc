Proceso insertar_elementos
	Definir coches, nuevo_elemento Como Caracter;
	Definir i, p Como Entero;
	
	Dimension coches[100];
	coches[1] <- "Alfa Romeo";
	coches[2] <- "Fiat";
	coches[3] <- "Ford";
	coches[4] <- "Lancia";
	coches[5] <- "Renault";
	coches[6] <- "Seat";
	coches[7] <- " ";
	coches[8] <- " ";
	coches[9] <- " ";
	
	Para i<-1 Hasta 7 Hacer
		Escribir Sin Saltar coches[i], " - ";
	FinPara
	
	Escribir "Posicion a insertar:";
	Leer P;
	i<-9
	Escribir "Ingrese la nueva marca:";
	Leer nuevo_elemento;
	
	Mientras i>=P Hacer
		
	FinMientras
	
FinProceso
