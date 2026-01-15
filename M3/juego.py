###Librerias###

import modulo_dic_fun as mod

###Variables###

flgs = True #flag para salir del programa
opc = 0 #opcion menu

###Juego###

while flgs:
    if opc == 0: #Menu principal
        opc = int(mod.getOpt( \
            "1)Login\n"+
            "2)Create user\n"+
            "3)Show Adventures\n"+
            "4)Exit",
            "Input Option: ",
            [1,2,3,4],["e","exit"]
            ))
    elif opc == 1: #Login
        chk = mod.checkUserbdd(input("Introduce tu usuario: "), input("Introduce tu contraseña: "))
        if chk == 1:
            print("inicias sesion")
            opc = 0
        elif chk == 0:
            print("El nombre de usuario que has introducido no existe")
            tmm = input("Quieres volver al menu principal?S/N: ")
            if tmm.lower() in (i.lower() for i in mod.yes):
                opc = 0
        else:
            print("Contraseña incorrecta")
            tmm = input("Quieres volver al menu principal?S/N: ")
            if tmm.lower() in (i.lower() for i in mod.yes):
                opc = 0
    elif opc == 2: #Crear usuario
        usr = input("Introduce el nombre de usuario: ")
        if mod.checkUser(usr):
            if mod.userExists(usr):
                print("el nombre de usuario ya existe, utiliza otro")
                tmm = input("Quieres volver al menu principal?S/N: ")
                if tmm.lower() in (i.lower() for i in mod.yes):
                    opc = 0
            else:
                flg_pswc = True
                while flg_pswc:
                    pswrd = input("Introduce la contraseña: ")
                    if mod.checkPassword:
                        pswrd2 = input("Introduce la contraseña otra vez: ")
                        if pswrd == pswrd2:
                            mod.insertUser("NULL",usr,pswrd)
                            print("Usuario creado")
                            opc = 0
                            flg_pswc = False
                        else:
                            print("La contraseña no coincide")
                            tmm = input("Quieres volver al menu principal?S/N: ")
                            if tmm.lower() in (i.lower() for i in mod.yes):
                                opc = 0
                                flg_pswc = False
                    else:
                        tmm = input("Quieres volver al menu principal?S/N: ")
                        if tmm.lower() in (i.lower() for i in mod.yes):
                            opc = 0
                            flg_pswc = False
    elif opc == 3:
        print()
        input("Press enter to continue...")
    elif opc == 4:
        print("Saliendo del juego")
        flgs = False