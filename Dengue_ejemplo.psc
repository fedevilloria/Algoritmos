Algoritmo Dengue_ejemplo
	
	Definir tucuman, buenos_aires, vacunas Como Entero;
	Definir tucuman_objetivo, buenos_aires_objetivo, vacunados_buenos_aires, vacunados_tucuman, vacunas_tucuman, vacunas_buenos_aires Como Real;
	
	//Poblacion de la provincia
	tucuman <- 848;
	buenos_aires <- 300;
	
	//Vacunas ingresadas al pais
	Leer vacunas;
	
	//Determinamos la poblacion objetivo en porcentaje:
	//Niños entre 4 - 12 años & Adultos > 60 años
	tucuman_objetivo <- 0.22;
	buenos_aires_objetivo <- 0.25;
	
	//Calculo de la poblacion objetivo en cada provincia
	vacunados_tucuman <- tucuman * tucuman_objetivo;
	vacunados_buenos_aires <- buenos_aires * buenos_aires_objetivo;
	
	//Calculo de la cantidad de vacunas a asignar para cada provincia
	vacunas_tucuman <- (vacunas * vacunados_tucuman / (vacunados_tucuman + vacunados_buenos_aires));
	vacunas_buenos_aires <- vacunas - vacunas_tucuman;
	
	Escribir vacunas_tucuman;
	Escribir vacunas_buenos_aires;
	
FinAlgoritmo