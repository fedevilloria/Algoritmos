Algoritmo Vectores
	Definir vector_ejemplo, i, elemento_mayor, elemento_menor, suma_elementos, contador_positivos, contador_negativos, contador_pares, contador_impares, elemento_posicion_par_mayor, elemento_posicion_par_menor, elemento_posicion_impar_mayor, elemento_posicion_impar_menor Como Entero;
	Definir promedio_elementos Como Real;
	
	
	//Dimensionar un vector
	Dimension vector_ejemplo[100];
	
	//Consigna para el 19: 
	//El mayor de las posiciones pares (check)
	//El menor de las posiciones pares (check)
	//Promedio de los elementos del vector (check)
	//El vector ordenado
	//El mayor de las posiciones impares (check)
	//El menor de las posiciones impares (check)
	//Cuantos elementos son pares (check)
	//Cuantos elementos son impares (check)
	//Cuantos elementos son negativos (check)
	//Cuantos elementos son positivos (check)
	//Estadistica sobre un vector

	
	//Cargar un vector
	Para i<-1 Hasta 5 Hacer
		Escribir "Ingrese el valor correspondiente a la posicion ", i;
		Leer vector_ejemplo[i];
		elemento_mayor <- vector_ejemplo[1];
		elemento_menor <- vector_ejemplo[1];
	FinPara
	
	//Inicializacion de variables
	elemento_mayor <- [1];
	elemento_menor <- [1];
	suma_elementos <- [0];
	elemento_posicion_par_mayor <- vector_ejemplo[2];
	elemento_posicion_par_menor <- vector_ejemplo[2];
	elemento_posicion_impar_mayor <- vector_ejemplo[1];
	elemento_posicion_impar_menor <- vector_ejemplo[1];
	promedio_elementos <- 0;
	contador_positivos <- 0;
	contador_negativos <- 0;
	contador_pares <- 0;
	contador_impares <- 0;
	
	
	//Recorrer un vector y obtener el mayor elemento
	Para i<-1 Hasta 5 Hacer
		
		Si vector_ejemplo[i] > elemento_mayor Entonces
			elemento_mayor <- vector_ejemplo[i];
		FinSi
		
	FinPara
	
	//Recorrer un vector y obtener el menor elemento
	Para i<-1 Hasta 5 Hacer
		
		Si vector_ejemplo[i] < elemento_menor Entonces
			elemento_menor <- vector_ejemplo[i];
		FinSi
		
	FinPara
	
	//Recorrer un vector, obtener la suma y realizar el promedio de sus elementos
	Para i<-1 Hasta 5 Hacer
		suma_elementos <- suma_elementos + vector_ejemplo[i];
		promedio_elementos <- suma_elementos / 5;
	FinPara
	
	//Recorrer un vector y obtener la cantidad de numeros positivos
	Para i<-1 Hasta 5 Hacer
		Si (vector_ejemplo[i]>0) Entonces
			contador_positivos <- contador_positivos + 1;
		FinSi
	FinPara
	
	//Recorrer un vector y obtener la cantidad de numeros negativos
	Para i<-1 Hasta 5 Hacer
		Si (vector_ejemplo[i]<0) Entonces
			contador_negativos <- contador_negativos + 1;
		FinSi
	FinPara
	
	//Recorrer un vector y obtener la cantidad de elementos pares e impares
	Para i<-1 Hasta 5 Hacer
		Si (vector_ejemplo[i] Mod 2 = 0) Entonces
			contador_pares <- contador_pares + 1;
		SiNo
			contador_impares <- contador_impares + 1;
		FinSi
	FinPara
	
	//Recorrer un vector y obtener el mayor de las posiciones pares e impares
	Para i<-1 Hasta 5 Hacer
		Si i MOD 2 = 0 Entonces
			Si vector_ejemplo[i] > elemento_posicion_par_mayor Entonces
				elemento_posicion_par_mayor <- vector_ejemplo[i];
			FinSi
		SiNo
			Si vector_ejemplo[i] > elemento_posicion_impar_mayor Entonces
				elemento_posicion_impar_mayor <- vector_ejemplo[i];
			FinSi
		FinSi
	FinPara
	
	//Recorrer un vector y obtener el menor de las posiciones pares e impares
	Para i<-1 Hasta 5 Hacer
		Si i MOD 2 = 0 Entonces
			Si vector_ejemplo[i] < elemento_posicion_par_menor Entonces
				elemento_posicion_par_menor <- vector_ejemplo[i];
			FinSi
		SiNo
			Si vector_ejemplo[i] < elemento_posicion_impar_menor Entonces
				elemento_posicion_impar_menor <- vector_ejemplo[i];
			FinSi
		FinSi
	FinPara
	
	//Imprimir un vector
	Para i<-1 Hasta 5 Hacer
		Escribir Sin Saltar vector_ejemplo[i], " - ";
	FinPara
	
	Escribir "                                          ";
	Escribir "El mayor elemento es: ", elemento_mayor;
	Escribir "El menor elemento es: ", elemento_menor;
	Escribir "La suma de los elementos es: ", suma_elementos;
	Escribir "El promedio de los elementos es: ", promedio_elementos;
	Escribir "La cantidad de elementos positivos son: ", contador_positivos;
	Escribir "La cantidad de elementos negativos son: ", contador_negativos;
	Escribir "La cantidad de elementos pares son: ", contador_pares;
	Escribir "La cantidad de elementos impares son: ", contador_impares;
	Escribir "El mayor de las posiciones pares es: ", elemento_posicion_par_mayor;
	Escribir "El menor de las posiciones pares es: ", elemento_posicion_par_menor;
	Escribir "El mayor de las posiciones impares es: ", elemento_posicion_impar_mayor;
	Escribir "El menor de las posiciones impares es: ", elemento_posicion_impar_menor;
	
FinAlgoritmo
	