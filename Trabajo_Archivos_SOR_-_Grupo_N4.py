def pantallaPrincipal(comandoUsuario): #Esta funcion nos va a mostrar la pantalla de logueo/registro
    while comandoUsuario!=str(3):
        print("*Ingrese 1 para loguearse\n*Ingrese 2 para registrarse\n*Ingrese 3 para cerrar el programa")
        comandoUsuario=str(input()) #Le mostramos al operador del programa las opciones que tiene
        if comandoUsuario!=str(1) and comandoUsuario!=str(2) and comandoUsuario!=str(3):
            print("Ingrese un comando valido") #Si ingresa un comando incorrecto le pedimos que lo vuelva a ingresar
        if comandoUsuario==str(1): #Si es uno devera ingresar sus datos para loguearse
            nombreUsuarioLoguearse=input("Ingrese su nombre de usuario: ")
            contraseñaUsuarioLoguearse=input("Ingrese su contraseña: ")
            datosComprobar=contraseñaUsuarioLoguearse+"\t"+nombreUsuarioLoguearse #Aqui guardamos los dos datos para poder compararlos con el archivo de usuarios
            archivo=open("archivo_Usuarios.txt","r")
            registroUsuario=archivo.readline() #Aqui sacamos los datos de un usuario
            condicionLogueo=int(0)
            while registroUsuario!="":
                infoUsuarioAux=registroUsuario[0:len(datosComprobar)] #En esta intruccion sacamos el usuario y ccontraseña extraidos del archivo
                if infoUsuarioAux==datosComprobar: #Los comparamos con los datos ingresados
                    registroUsuarioAux=registroUsuario #En caso de ser iguales guardamos los datos para luego realizar la autocompletacion en la carga de denuncia
                    longContraseña=len(contraseñaUsuarioLoguearse) #Sacamos la longitud de la cadena para luego extraerla del registro
                    pantallaSecundaria(registroUsuarioAux,longContraseña)
                    registroUsuario=""
                    condicionLogueo=int(1)
                registroUsuario=archivo.readline() #Esta instruccion sirve para leer una nueva linea de usuario
            if condicionLogueo==0:
                print("Su usuario y/o contraseña son incorrectos") #En caso de que no se encuentre el usuario y/o la contraseña se mostrara un mensaje
        if comandoUsuario==str(2): 
            RegistrarUsuario()
def pantallaSecundaria(registroUsuarioAux,longContraseña):
    #Esta funcion lo que hace es mostrarle al usuario ya logueado los comandos disponibles
    print("*Si desea cargar una nueva denuncia ingrese 1\n*Si desea visualizar una denuncia ingrese 2\n*Si desea volver al menu loguearse/registrarse ingrese 3")
    condicionPrograma=int(input()) #Dentro de un print ponemos los comandos que puede utilizar el usuario
    if condicionPrograma!=1 and condicionPrograma!=2 and condicionPrograma!=3:
            print("Por favor ingrese un comando valido") #En caso de no usar un comando previamente registrado aparece este mensaje
    if condicionPrograma==1:                    #En caso de ingresar 1 se dirigira al usuario a la pantalla de carga de datos de una denuncia
        archivo=open("cant_De_Denuncias.txt","r") 
        cantDeDenunciasAux=archivo.readline() #Aqui leemos el registro completo del archivo de denuncias realizadas
        archivo.close()
        longAux=len(cantDeDenunciasAux) #Averiguamos su longitud total
        cantDeDenunciasAux=str(cantDeDenunciasAux[i:longAux]) #Y hacemos una subcadena para sacar el numero, esto lo realizamos de esta forma
                                                              #ya que sacando el registro completo no nos tomaba como una cadena
        cantDeDenuncias=int(cantDeDenunciasAux) #Aqui hacemos entero el valor para poder operarlo 
        cantDeDenuncias=cantDeDenuncias+1       #Le sumamos +1
        cantDeDenuncias=str(cantDeDenuncias)    #La volvemos a pasar a cadena para guardarla en el archivo
        archivo=open("cant_De_Denuncias.txt","w")
        archivo.write(cantDeDenuncias) #Abrimos el archivo en formato 'w' para que sobreescriba el numero
        archivo.close()
        CargarDenuncia(cantDeDenuncias,registroUsuarioAux,longContraseña)
    if condicionPrograma==2:
        BuscarDenuncia(registroUsuarioAux,longContraseña) #Si el usuario ingresa 2 iremos a la pantalla de buscar denuncia
def RegistrarUsuario():
    archivo=open("archivo_Usuarios.txt","a+")
    nombreUsuario=input("Ingrese su nombre y apellido: ") #Al crear el archivo en modo 'a' o 'a+' tenemos la opcion de agregar datos
    contraseña=input("Ingrese su contraseña: ")           #Sin sobreescribir los anteriores
    tipoDNI=input("Ingrese el tipo de su DNI: ")
    numDNI=input("Ingrese su numero de DNI sin comas ni puntos: ")
    correoUsuario=input("Ingrese su correo electronico: ")
    archivo.write(contraseña+"\t"+nombreUsuario+"\t"+tipoDNI+"\t"+numDNI+"\t"+correoUsuario+"\n")
    archivo.close() #Ingresamos los datos al mismo tiempo separados por tabulaciones y al final con un enter
def CargarDenuncia(cantDeDenuncias,registroUsuarioAux,longContraseña): #En esta funcion cargamos una nueva denuncia
    vectorDatosDenuncia=["Escribe la fecha de la denuncia","Escribe nombre completo del denunciado (En caso de no conocerlo ingrese Desconocido)","Escribe la localidad del hecho ilicito","Escribe el tipo de denuncia (Hidrica, Fauna, Forestal, Reserva Naturales)","Escribe la descripcion de la denuncia"]
    cantDeDenuncias=str(cantDeDenuncias) #Hacemos string el numero de la cantidad de denuncias
    longCantDenuncias=len(cantDeDenuncias) #Sacamos la cantidad de caracteres que posee el numero
    cantDeCeros=4-longCantDenuncias #A esta cantidad de caracteres se la restamos a 4 ya que nuestro numero de denuncia
    archivo=open("archivo_Denuncias.txt","a+") # y esa va a ser la cantidad de 0 que le vamos a agregar adelante
    numDenunciaMostrar=str("") #Esta variable sirve para luego mostrar el numero de denuncia generado
    if cantDeCeros>0:
        for i in range(0,cantDeCeros): #Aqui imprimimos los 0
            archivo.write("0")
            numDenunciaMostrar=numDenunciaMostrar+"0"
    archivo.write(cantDeDenuncias+"\t") #Esto es para guardar el numero de denuncia ya creado
    numDenunciaMostrar=numDenunciaMostrar+cantDeDenuncias #Generamos el numero de denuncia a mostrar
    archivo.write(registroUsuarioAux[longContraseña+1:len(registroUsuarioAux)-1]+"\t") #En  esta instruccion autocompletamos los datos del usuario
    for i in range(0,5):
        print(vectorDatosDenuncia[i])
        cadena=input()
        archivo.write(cadena+"\t")
    archivo.write("\n") #Imprimimos un enter para que la proxima denuncia se guarde en el renglon de abajo
    archivo.close()
    print("El numero de la denuncia anteriormente cargada es: ", numDenunciaMostrar)
    pantallaSecundaria(registroUsuarioAux,longContraseña)
def BuscarDenuncia(registroUsuarioAux,longContraseña): #En esta funcion buscamos una denuncia en base a su codigo
    estadoDeBusqueda=int(0)
    archivo=open("archivo_Denuncias.txt","r")
    print("Ingrese el numero de denuncia que desea visualizar")
    numeroDeDenunciaBuscar=str(input()) #Ingresamos el numero de denuncia que deseamos visualizar por ejemplo 0014
    contenido=archivo.readline()
    while contenido!="":
        numDeDenunciaArchivo=contenido[0:4] #Aqui extremos el numero de denuncia del registro
        if numeroDeDenunciaBuscar==numDeDenunciaArchivo: #Lo comparamos con el numero ingresado
            print(contenido) #Si es igual mostramos la denuncia 
            contenido=""
            estadoDeBusqueda=int(1) #Y actualizamos el estado de la busqueda a 1
        contenido=archivo.readline()
    archivo.close()
    if estadoDeBusqueda==0: #Si al final el estado de la busqueda queda en 0 se mostrara el mensaje siguiente
        print("El codigo de denuncia ingresado no es valido")
    pantallaSecundaria(registroUsuarioAux,longContraseña)
i=int(0)
archivo=open("cant_De_Denuncias.txt","a") #Archivo para guardar la cantidad de denuncias totales
archivo.close()
archivo=open("cant_De_Denuncias.txt","r")
conteoDenunciasAux=archivo.readline()
archivo.close()
if conteoDenunciasAux=="": #En caso de que el archivo este vacio, aqui inicializamos la cantidad de denuncias en 0, esto lo realizaremos una sola vez
    archivo=open("cant_De_Denuncias.txt","a") 
    print("Ingrese un 0")
    numInicial=input()
    archivo.write(numInicial)
    archivo.close()
comandoUsuario=str(0)
condicionPrograma=int(0)
if condicionPrograma==0:
    pantallaPrincipal(comandoUsuario)
    condicionPrograma=int(1)