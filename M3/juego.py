###Librerias###

import modulo_dic_fun as mod

###Variables###

flgs = True #flag para salir del programa
opc = 0 #opcion menu
flg_log = False #Flag de login

###Juego###

while flgs:
    if opc == 0: #Menu principal
        if flg_log == False:
            opc = int(mod.getOpt( \
                "1)Login\n"+
                "2)Create user\n"+
                "3)Replay Adventure\n"+
                "4)Reports\n"+
                "5)Exit",
                "Input Option: ",
                [1,2,3,4,5],["e","exit"]
                ))
        else:
            opc = int(mod.getOpt( \
                "1)Logout\n"+
                "2)Play\n"+
                "3)Replay Adventure\n"+
                "4)Reports\n"+
                "5)Exit",
                "Input Option: ",
                [1,2,3,4,5],["e","exit"]
                ))
    elif opc == 1: #Login/Logout
        if flg_log: #Logout
            flg_log = False
            mod.game_context["idUser"] = ""
            mod.game_context["user"] = ""
            print("Te has deslogeado")
            opc = 0
        else: #Login
            usr = input("Introduce tu usuario: ")
            pswrd = input("Introduce tu contraseña: ")
            chk = mod.checkUserbdd(usr, pswrd)
            if chk == 1:
                mod.game_context["user"] = usr
                idu = mod.get_table(\
                    "SELECT idUser" \
                    " FROM user" \
                    f" WHERE Username = '{usr}'")
                mod.game_context["idUser"] = idu[0][0]
                print("inicias sesion")
                flg_log = True
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
    elif opc == 2: #Crear usuario/ Jugar
        if flg_log == False: #Crear usuario
            usr = input("Introduce el nombre de usuario (6-10 Characters AlphaNum): ")
            if mod.checkUser(usr):
                if mod.userExists(usr):
                    print("El nombre de usuario ya existe, utiliza otro")
                    tmm = input("Quieres volver al menu principal?S/N: ")
                    if tmm.lower() in (i.lower() for i in mod.yes):
                        opc = 0
                else:
                    flg_pswc = True
                    while flg_pswc:
                        pswrd = input("Introduce la contraseña (8-12 characters and minimum, 1 Uppercase, 1 Lowercase, 1 Num, 1 Special): ")
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
        else: #Juego
            print("Juego")
    elif opc == 3: #Replay Adventure
        input("Press enter to continue...")
    elif opc == 4: #Reports
        input("Press enter to continue...")
    elif opc == 5: #Salir
        print("Saliendo del juego")
        flgs = False