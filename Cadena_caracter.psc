Proceso Cadena_caracter
	Definir narrativa1, sub_cadena, narrativa2, union, may, min, conversion_texto Como Caracter;
	Definir long1, long2, conversion_numero, suma Como Entero;
	Escribir "Sr. Usuario, ingrese una cadena de caracter:";
	Leer narrativa1;
	Escribir narrativa1;
	Escribir " ";
	Escribir "Sr. Usuario, ingrese una cadena de caracter:";
	Leer narrativa2;
	Escribir narrativa2;
	
	long1 <- Longitud(narrativa1);
	Escribir long1;
	
	long2 <- Longitud(narrativa2);
	Escribir long2;
	
	sub_cadena <- SubCadena(narrativa1,0,10);
	Escribir sub_cadena;
	
	union <- Concatenar(narrativa1,narrativa2);
	Escribir union;
	
	may <- Mayusculas(narrativa1);
	min <- Minusculas(narrativa1);
	Escribir may;
	Escribir min;
	
	conversion_numero <- ConvertirANumero(narrativa1);
	Escribir conversion_numero;
	suma <- conversion_numero + 1950;
	Escribir suma;
	
	conversion_texto <- ConvertirATexto(suma);
	Escribir conversion_texto;
FinProceso
