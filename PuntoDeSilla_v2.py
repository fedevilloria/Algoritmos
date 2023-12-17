# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	matriza = int()
	i = int()
	filas = int()
	j = int()
	columnas = int()
	num = int()
	maximo_fila = int()
	minimo_columna = int()
	maximo_columna = int()
	minimo_fila = int()
	contador = int()
	auxiliar = int()
	punto_silla = int()
	matriza = [[int() for ind0 in range(100)] for ind1 in range(100)]
	maximo_fila = [int() for ind0 in range(100)]
	minimo_columna = [int() for ind0 in range(100)]
	maximo_columna = [int() for ind0 in range(100)]
	minimo_fila = [int() for ind0 in range(100)]
	punto_silla = [int() for ind0 in range(100)]
	maximo_fila[1] = -999
	maximo_fila[2] = -999
	maximo_fila[3] = -999
	maximo_fila[4] = -999
	maximo_fila[5] = -999
	maximo_fila[6] = -999
	maximo_fila[7] = -999
	maximo_fila[8] = -999
	minimo_columna[1] = 999
	minimo_columna[2] = 999
	minimo_columna[3] = 999
	minimo_columna[4] = 999
	minimo_columna[5] = 999
	minimo_columna[6] = 999
	minimo_columna[7] = 999
	minimo_columna[8] = 999
	maximo_columna[1] = -999
	maximo_columna[2] = -999
	maximo_columna[3] = -999
	maximo_columna[4] = -999
	maximo_columna[5] = -999
	maximo_columna[6] = -999
	maximo_columna[7] = -999
	maximo_columna[8] = -999
	minimo_fila[1] = 999
	minimo_fila[2] = 999
	minimo_fila[3] = 999
	minimo_fila[4] = 999
	minimo_fila[5] = 999
	minimo_fila[6] = 999
	minimo_fila[7] = 999
	minimo_fila[8] = 999
	for i in range(1,91):
		punto_silla[i] = 0
	filas = int(input())
	columnas = int(input())
	while filas!=0 and columnas!=0:
		# Cargar la matriz e imprimirla
		for i in range(1,filas+1):
			for j in range(1,columnas+1):
				matriza[i][j] = int(input())
		# Maximo de fila y minimo de columna
		for i in range(1,filas+1):
			for j in range(1,columnas+1):
				if matriza[i][j]>maximo_fila[i]:
					maximo_fila[i] = matriza[i][j]
				if matriza[i][j]<minimo_columna[j]:
					minimo_columna[j] = matriza[i][j]
		for i in range(1,filas+1):
			for j in range(1,columnas+1):
				if matriza[i][j]>maximo_columna[j]:
					maximo_columna[j] = matriza[i][j]
				if matriza[i][j]<minimo_fila[i]:
					minimo_fila[i] = matriza[i][j]
		contador = 0
		for i in range(1,filas+1):
			for j in range(1,columnas+1):
				if maximo_fila[i]==minimo_columna[j] or maximo_columna[j]==minimo_fila[i]:
					punto_silla[contador] = 1
				else:
					punto_silla[contador] = 0
		maximo_fila[1] = -999
		maximo_fila[2] = -999
		maximo_fila[3] = -999
		maximo_fila[4] = -999
		maximo_fila[5] = -999
		maximo_fila[6] = -999
		maximo_fila[7] = -999
		maximo_fila[8] = -999
		minimo_columna[1] = 999
		minimo_columna[2] = 999
		minimo_columna[3] = 999
		minimo_columna[4] = 999
		minimo_columna[5] = 999
		minimo_columna[6] = 999
		minimo_columna[7] = 999
		minimo_columna[8] = 999
		maximo_columna[1] = -999
		maximo_columna[2] = -999
		maximo_columna[3] = -999
		maximo_columna[4] = -999
		maximo_columna[5] = -999
		maximo_columna[6] = -999
		maximo_columna[7] = -999
		maximo_columna[8] = -999
		minimo_fila[1] = 999
		minimo_fila[2] = 999
		minimo_fila[3] = 999
		minimo_fila[4] = 999
		minimo_fila[5] = 999
		minimo_fila[6] = 999
		minimo_fila[7] = 999
		minimo_fila[8] = 999
		contador = contador+1
		filas = int(input())
		columnas = int(input())
	for i in range(1,punto_silla[i]+1):
		if punto_silla[i]==1:
			print("SI")
		else:
			print("NO")

