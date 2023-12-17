personas = []
matriz_usuarios = []
print("Bienvenido al programa de manejo de usuario\nPor favor, inicie sesión. Si no tiene una cuenta puede crearse una.")
decision = 1
while decision != 0:
    print("Digite lo que desea realizar")
    print("1-Iniciar sesión\n2-Registrarse\n0-Salir")
    decision = int(input())
    if decision != 0 and decision != 1 and decision != 2: # Verificación para que el usuario ingrese solo un número válido.
        print("Por favor, ingrese un valor correspondiente a las opciones")
    else:
        if decision == 1: # Si el usuario decide iniciar sesión le pido los datos, una vez ingresados los datos, si los mismos se encuentran en la matriz de los usuarios
                          # procede al menú para las siguientes elecciones.
           email = input("Email: ")
           contrasena = input("Contraseña: ")

           if email in personas and contrasena in matriz_usuarios:
               menu_usuario = 1
               while menu_usuario != 0:
                   print("Digite lo que desea realizar")
                   print("1-Visualizar perfil\n2-Modificar perfil\n0-Salir")

                   #Para que el usuario tenga la libertad de poder elegir las opciones hice otro menú, el cual lo va corriendo de la misma forma que el anterior.
                   menu_interno_decision = int(input())
                   if menu_interno_decision != 0 and menu_interno_decision != 1 and menu_interno_decision != 2: # Verificación para que el usuario ingrese solo un número válido.
                       print("Por favor, ingrese un valor correspondiente a las opciones")

                   else:
                       if menu_interno_decision == 1:
                           print(f"Nombre y Apellido: {personas[2]}\nD.N.I.: {personas[3]}\nEmail: {personas[0]}\nContraseña: {personas[1]}")

                       elif menu_interno_decision == 2:
                           print("Digite lo que desea modificar")
                           print("1-Nombre y Apellido\n2-D.N.I.\n3-Email\n4-Contraseña\n0-Salir")

                           # Para que el usuario tenga la libertad de poder elegir las opciones hice otro menú, el cual lo va corriendo de la misma forma que el anterior.
                           menu_modificaciones = 1
                           while menu_modificaciones != 0:
                               menu_modificaciones = int(input())

                               if menu_modificaciones == 1:
                                   nombre_apellido = input("Nombre y apellido: ")
                                   personas[2] = nombre_apellido
                                   print("Nombre cambiado con éxito. Digite 0 para volver")

                               elif menu_modificaciones == 2:
                                   documento = input("D.N.I.: ")
                                   personas[3] = documento
                                   print("Documento cambiado con éxito. Digite 0 para volver")

                               elif menu_modificaciones == 3:
                                   email = input("Email: ")
                                   contrasena = input("Ingrese su contraseña para efectuar el cambio: ")
                                   if contrasena in personas:
                                       personas[0] = email
                                       print("Email cambiado con éxito. Digite 0 para volver")
                                   else:
                                       print("Ha ingresado mal su contraseña.")

                               elif menu_modificaciones == 4:
                                   contrasena_actual = print("Ingrese su contraseña actual: ")
                                   if contrasena_actual == contrasena: # Verificación para que las contraseña ingresada sea igual a la contraseña original del usuario.
                                       nueva_contrasena = print("Contraseña nueva: ")
                                       nueva_contrasena_verificacion = print("Ingrese nuevamente la contraseña: ")
                                       if nueva_contrasena == nueva_contrasena_verificacion: # Verificación para que las contraseñas sean iguales.
                                           contrasena = nueva_contrasena
                                           personas[1] = contrasena
                                           print("Contraseña cambiada con éxito. Digite 0 para volver")
                                       else:
                                           print("Las contraseñas no coinciden.")

                               elif menu_modificaciones == 0: # Hago 0 al menú para poder salir del mismo e ir al menú anterior.
                                   menu_modificaciones = 0

                       elif menu_interno_decision == 0: # Hago 0 al menú principal para poder salir del programa.
                           menu_usuario = 0
           else:
               print("No coinciden con un usuario registrado.")

        elif decision == 2:
            email = input("Ingrese su email: ")
            personas = personas + [email]
            contrasena = input("Ingrese su contraseña: ")
            validacion_contrasena = input("Por favor, ingrese nuevamente su contraseña: ")

            if contrasena == validacion_contrasena:
                personas = personas + [contrasena]
                nombre_apellido = input("Ingrese su nombre y apellido: ")
                personas = personas + [nombre_apellido]
                documento = input("Ingrese su D.N.I.: ")
                personas = personas + [documento]
                matriz_usuarios = matriz_usuarios + [personas]
            else:
                print("Las contraseñas no coinciden, por favor ingresela de nuevo.")