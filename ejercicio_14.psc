Proceso ejercicio_14
	Definir legajo Como Entero;
	Definir promedio, nota1, nota2, nota3, nota4 Como Real;
	promedio <- 0;
	Escribir "Ingrese el legajo.";
	Leer legajo;
	Mientras legajo <> 0 Hacer
		Escribir "Nota 1:";
		Leer nota1;
		Escribir "Nota 2:";
		Leer nota2;
		Escribir "Nota 3:";
		Leer nota3;
		Escribir "Nota 4:";
		Leer nota4;
		promedio <- (nota1 + nota2 + nota3 + nota4) / 4;
		Escribir "Si desea ingresar otro legajo, ingreselo, si no ingrese 0";
		Leer legajo;
	FinMientras
	Escribir promedio;
FinProceso
