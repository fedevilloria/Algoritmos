Proceso ejercicio_11
	Definir mayor_vendedor, menor_vendedor, vendedor1, vendedor2, vendedor3, vendedor4 Como Entero;
	Definir importe, importe_bajo, importe_alto, importe_vendedor1, importe_vendedor2, importe_vendedor3, importe_vendedor4 Como Real;
	importe_bajo <- 0;
	importe_alto <- 0;
	mayor_vendedor <- 0;
	menor_vendedor <- 0;
	importe_vendedor1 <- 1;
	importe_vendedor2 <- 1;
	importe_vendedor3 <- 1;
	importe_vendedor4 <- 1;
	
	///INCOMPLETO

	Mientras importe_vendedor1 <> 0 o importe_vendedor2 <> 0 o importe_vendedor3 <> 0 o importe_vendedor4 <> 0 Hacer
		Escribir "Ingrese el codigo del vendedor 1 y su importe:";
		Leer vendedor1;
		Leer importe_vendedor1;
		
		Escribir "Ingrese el codigo del vendedor 2 y su importe:";
		Leer vendedor2;
		Leer importe_vendedor2;
		
		Escribir "Ingrese el codigo del vendedor 3 y su importe:";
		Leer vendedor3;
		Leer importe_vendedor3;
		
		Escribir "Ingrese el codigo del vendedor 4 y su importe:";
		Leer vendedor4;
		Leer importe_vendedor4;
		
		Si importe_vendedor1 < importe_vendedor2 y importe_vendedor1 < importe_vendedor3 y importe_vendedor1 < importe_vendedor4 Entonces
			importe_bajo <- importe_vendedor1;
			menor_vendedor <- vendedor1;
		SiNo
			si	importe_vendedor1 > importe_vendedor2 y importe_vendedor1 > importe_vendedor3 y importe_vendedor1 > importe_vendedor4 Entonces
				importe <- importe_vendedor1;
				mayor_vendedor <- vendedor1;
			FinSi
		FinSi
		
		Si importe_vendedor2 < importe_vendedor1 y importe_vendedor2 < importe_vendedor3 y importe_vendedor2 < importe_vendedor4 Entonces
			importe_bajo <- importe_vendedor2;
			menor_vendedor <- vendedor2;
		SiNo
			si	importe_vendedor2 > importe_vendedor1 y importe_vendedor2 > importe_vendedor3 y importe_vendedor2 > importe_vendedor4 Entonces
				importe <- importe_vendedor2;
				mayor_vendedor <- vendedor2;
			FinSi
		FinSi
		
		Si importe_vendedor3 < importe_vendedor1 y importe_vendedor3 < importe_vendedor2 y importe_vendedor1 < importe_vendedor4 Entonces
			importe_bajo <- importe_vendedor3;
			menor_vendedor <- vendedor3;
		SiNo
			si	importe_vendedor3 > importe_vendedor1 y importe_vendedor3 > importe_vendedor2 y importe_vendedor3 > importe_vendedor4 Entonces
				importe <- importe_vendedor3;
				mayor_vendedor <- vendedor3;
			FinSi
		FinSi
		
		Si importe_vendedor4 < importe_vendedor1 y importe_vendedor4 < importe_vendedor2 y importe_vendedor4 < importe_vendedor3 Entonces
			importe_bajo <- importe_vendedor4;
			menor_vendedor <- vendedor4;
		SiNo
			si	importe_vendedor4 > importe_vendedor1 y importe_vendedor4 > importe_vendedor2 y importe_vendedor4 > importe_vendedor3 Entonces
				importe <- importe_vendedor4;
				mayor_vendedor <- vendedor4;
			FinSi
		FinSi
		
	FinMientras
	Escribir "El mayor importe es: ", importe_alto, " y el vendedor fue ", mayor_vendedor;
	Escribir "El menor importe es: ", importe_bajo, " y el vendedor fue ", menor_vendedor;
	
FinProceso
