Proceso PreParcial_2
	Definir VectorA, VectorB, i, num, reemplazo Como Entero;
	
	Dimension VectorA[100];
	Dimension VectorB[100];
	
	//Cargar el vector
	Para i<-1 Hasta 6 Hacer
		Escribir "Ingrese un numero:";
		Leer VectorA[i];
	FinPara
	
	Para i<-1 Hasta 6 Hacer
		Escribir Sin Saltar VectorA[i], " - ";
	FinPara
	
	Escribir " ";
	
	//Cifrado del vector
	reemplazo <- 0;
	Para i<-2 Hasta 5 Hacer
		reemplazo <- VectorA[i] - VectorA[i-1];
		Si reemplazo < 0 Entonces
			VectorB[i] <- reemplazo + 255;
		SiNo
			VectorB[i] <- reemplazo;
		FinSi
	FinPara
	
FinProceso
