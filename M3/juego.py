###Librerias###

import modulo_dic_fun as mod

###Variables###

flgs = True #flag para salir del programa
opc = 0 #opcion menu
opcr = 0 #opcion menu reports
flg_log = False #Flag de login

###Juego###

while flgs:
    if opc == 0: #Menu principal
        if flg_log == False:
            opc = int(mod.getOpt("""
                1)Login\n
                2)Create user\n
                3)Replay Adventure\n
                4)Reports\n
                5)Exit""",
                "Input Option: ",
                [1,2,3,4,5],["e","exit"]
                ))
        else:
            opc = int(mod.getOpt("""
                1)Logout\n
                2)Play\n
                3)Replay Adventure\n
                4)Reports\n
                5)Exit""",
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
                    "SELECT idUser " \
                    "FROM user " \
                    f"WHERE Username = '{usr}'")
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
        opcr = int(mod.getOpt("""
                1)Most used answer\n
                2)Player with more games played\n
                3)Games played by user\n
                4)Back""",
                "Input Option: ",
                [1,2,3,4],["","back"]
                ))
        if opcr == 1:
            answer = mod.get_table("""
                SELECT 'ID Aventura', 'Nombre Aventura', 'ID Step', 'Descripción Step', 'ID Answer', 'Descripción Answer', 'Veces escogida'
                UNION ALL
                SELECT adv.idAdventure, adv.Name, bs.idByStep_Adventure, bs.Description, ans.idAnswers_ByStep_Adventure, ans.Description,
                COUNT(c.idAnswers_ByStep_Adventure) AS repeticiones
                FROM answers_bystep_adventure ans
                JOIN bystep_adventure bs ON ans.idByStep_Adventure = bs.idByStep_Adventure
                JOIN adventure adv ON bs.idAdventure = adv.idAdventure
                LEFT JOIN choices c ON ans.idAnswers_ByStep_Adventure = c.idAnswers_ByStep_Adventure
                GROUP BY adv.idAdventure, adv.Name, bs.idByStep_Adventure, bs.Description, ans.idAnswers_ByStep_Adventure, ans.Description
                ORDER BY repeticiones DESC
                """)
            print(mod.getFormatedTable(answer, "Most used answer"))
            input("Press enter to continue...")
        elif opcr == 2:
            answer = mod.get_table("""
                SELECT 'Nombre de usuario', 'Partidas Jugadas'
                UNION ALL
                SELECT u.Username, COUNT(g.idGame) AS partidas_jugadas
                FROM user u
                JOIN game g ON u.idUser = g.idUser
                GROUP BY u.idUser, u.Username
                ORDER BY partidas_jugadas DESC
                LIMIT 1
                """)
            print(mod.getFormatedTable(answer, "Player with more games played"))
            input("Press enter to continue...")
        elif opcr == 3: 
            usr = input("De que usuario quieres ver las partidas?: ")
            answer = mod.get_table( """
                SELECT 'ID Aventura', 'Nombre Aventura', 'Fecha' 
                UNION ALL 
                SELECT adv.idAdventure, adv.Name, g.Date 
                FROM user u 
                JOIN game g ON u.idUser = g.idUser 
                JOIN adventure adv ON g.idAdventure = adv.idAdventure 
                WHERE u.Username = '%s' 
                ORDER BY g.Date DESC
                """)%usr
            print(mod.getFormatedTable(answer, f"Games played by {usr}"))
            input("Press enter to continue...")
        elif opcr == 4:
            opc = 0
    elif opc == 5: #Salir
        print("Saliendo del juego")
        flgs = False