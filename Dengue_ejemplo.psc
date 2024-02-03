Algoritmo Dengue_ejemplo
	
	Definir tucuman, buenos_aires, cordoba, santiago_del_estero, jujuy, santa_fe, chaco, catamarca, vacunas, verificacion, cod_provincia Como Entero;
	Definir densidad_tuc, densidad_ba, densidad_cba, densidad_sgo, densidad_jujuy, densidad_stafe, densidad_chaco, densidad_catamarca , densidad_total Como Real;
	Definir contagios_tuc, contagios_ba, contagios_cba, contagios_sgo, contagios_jujuy, contagios_stafe, contagios_chaco, contagios_catamarca Como Real;
	Definir vacunas_tuc, vacunas_ba, vacunas_cba, vacunas_sgo, vacunas_jujuy, vacunas_stafe, vacunas_chaco, vacunas_catamarca como Real;
	
	//Inicializacion de variables
	verificacion <- 1;
	
	densidad_total <- 0;
	densidad_ba <- 0;
	densidad_catamarca <- 0;
	densidad_tuc <- 0;
	densidad_cba <- 0;
	densidad_sgo <- 0;
	densidad_jujuy <- 0;
	densidad_stafe <- 0;
	densidad_chaco <- 0;
	
	contagios_ba <- 0;
	contagios_catamarca <- 0;
	contagios_cba <- 0;
	contagios_sgo <- 0;
	contagios_jujuy <- 0;
	contagios_stafe <- 0;
	contagios_chaco <- 0;
	contagios_tuc <- 0;
	
	//Poblacion de la provincia
	tucuman <- 1703186;
	buenos_aires <- 17569053;
	cordoba <- 3978984;
	santiago_del_estero <- 1054028;
	jujuy <- 797955;
	santa_fe <- 3556522;
	chaco <- 1142963;
	catamarca <- 429556;
	
	//Ingreso de datos: población contagiada. 
	Mientras verificacion <> 0 y verificacion = 1 Hacer
		Escribir "Ingrese el código de la provincia:";
		Escribir "1) Buenos Aires";
		Escribir "2) Córdoba";
		Escribir "3) Santa Fe";
		Escribir "4) Catamarca";
		Escribir "5) La Rioja";
		Escribir "6) Mendoza";
		Escribir "7) San Juan";
		Escribir "8) La Pampa";
		Escribir "9) Tucumán";
		Escribir "10) Formosa";
		Escribir "11) Chaco";
		Escribir "12) Misiones";
		Escribir "13) Entre Rios";
		Escribir "14) Corrientes";
		Escribir "15) San Luis";
		Escribir "16) Salta";
		Escribir "17) Jujuy";
		Escribir "18) Neuquén";
		Escribir "19) Rio Negro";
		Escribir "20) Chubut";
		Escribir "21) Santa Cruz";
		Escribir "22) Tierra del Fuego";
		Escribir "23) Santiago del Estero";
		Leer cod_provincia;
		Si cod_provincia = 13 o cod_provincia = 8 o cod_provincia = 6 o cod_provincia = 7 o cod_provincia = 15 o cod_provincia = 16 o cod_provincia = 5 o cod_provincia = 12 o cod_provincia = 14 o cod_provincia = 10 o cod_provincia = 19 o cod_provincia = 18 o cod_provincia = 20 o cod_provincia = 21 o cod_provincia = 22 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Su provincia no se encuentra en riesgo.";
		FinSi
		
		Si cod_provincia = 1 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios en Buenos Aires:";
			Leer contagios_ba;
		FinSi
		
		Si cod_provincia = 2 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios de Córdoba: ";
			Leer contagios_cba;
		FinSi
		
		Si cod_provincia = 3 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios de Santa Fe: ";
			Leer contagios_stafe;
		FinSi
		
		Si cod_provincia = 9 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios de Tucumán: ";
			Leer contagios_tuc;
		FinSi
		
		Si cod_provincia = 23 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios de Santiago del Estero: ";
			Leer contagios_sgo;
		FinSi
		
		Si cod_provincia = 17 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios de Jujuy: ";
			Leer contagios_jujuy;
		FinSi
		
		Si cod_provincia = 4 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios de Catamarca: ";
			Leer contagios_catamarca;
		FinSi
		
		Si cod_provincia = 11 Entonces
			Escribir "---------------------------------------------------------------------------------------------";
			Escribir "Ingrese la cantidad de contagios de Chaco: ";
			Leer contagios_chaco;
		FinSi
		Escribir "---------------------------------------------------------------------------------------------";
		Escribir "Desea seguir cargando datos?";
		Escribir "Ingrese 1 en caso de ser afirmativo";
		Escribir "Ingrese 0 en caso de ser negativo";
		Leer verificacion;
	FinMientras
	
	//Calculo de densidad de contagiados en relacion a la poblacion por provincia
	densidad_ba <- contagios_ba / buenos_aires;
	densidad_cba <- contagios_cba / cordoba;
	densidad_tuc <- contagios_tuc / tucuman;
	densidad_catamarca <- contagios_catamarca / catamarca;
	densidad_stafe <- contagios_stafe / santa_fe;
	densidad_sgo <- contagios_sgo / santiago_del_estero;
	densidad_jujuy <- contagios_jujuy / jujuy;
	densidad_chaco <- contagios_chaco / chaco;
	densidad_total <- densidad_ba + densidad_catamarca + densidad_cba + densidad_chaco + densidad_jujuy + densidad_sgo + densidad_stafe + densidad_tuc;
	
	//Vacunas ingresadas al pais
	Escribir "Ingrese la cantidad de vacunas ingresadas al país:";
	Leer vacunas;
	Escribir "---------------------------------------------------------------------------------------------";
	
	//Calculo de la poblacion objetivo en cada provincia
	vacunas_tuc <- (densidad_tuc / densidad_total) * vacunas;
	vacunas_ba <- (densidad_ba / densidad_total)  * vacunas;
	vacunas_cba <- (densidad_cba / densidad_total) * vacunas;
	vacunas_catamarca <- (densidad_catamarca / densidad_total) * vacunas;
	vacunas_chaco <- (densidad_chaco / densidad_total) * vacunas;
	vacunas_jujuy <- (densidad_jujuy / densidad_total) * vacunas;
	vacunas_sgo <- (densidad_sgo / densidad_total) * vacunas;
	vacunas_stafe <- (densidad_stafe / densidad_total) * vacunas;
	
	//Salida con los porcentajes obtenidos para repartir las vacunas ingresadas
	Escribir "Según los datos obtenidos a cada provincia le corresponde:";
	Escribir "Buenos Aires: ", trunc(vacunas_ba * 100 / vacunas), "%", " que corresponden a ", trunc(vacunas_ba), " vacunas.";
	Escribir "Catamarca: ", trunc(vacunas_catamarca * 100 / vacunas),"%", " que corresponden a ", trunc(vacunas_catamarca), " vacunas.";
	Escribir "Córdoba: ", trunc(vacunas_cba * 100 / vacunas),  "%", " que corresponden a ", trunc(vacunas_cba), " vacunas.";
	Escribir "Chaco: ", trunc(vacunas_chaco * 100 / vacunas), "%", " que corresponden a ", trunc(vacunas_chaco), " vacunas.";
	Escribir "Jujuy: ", trunc(vacunas_jujuy * 100 / vacunas), "%", " que corresponden a ", trunc(vacunas_jujuy), " vacunas.";
	Escribir "Santa Fe: ", trunc(vacunas_stafe * 100 / vacunas), "%", " que corresponden a ", trunc(vacunas_stafe), " vacunas.";
	Escribir "Santiago del Estero: ", trunc(vacunas_sgo * 100 / vacunas), "%", " que corresponden a ", trunc(vacunas_sgo), " vacunas.";
	Escribir "Tucumán: ", trunc(vacunas_tuc * 100 / vacunas), "%", " que corresponden a ", trunc(vacunas_tuc), " vacunas.";
	
FinAlgoritmo