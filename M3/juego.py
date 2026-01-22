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
            opc = int(mod.getOpt( \
                "1)Login\n"
                "2)Create user\n"
                "3)Replay Adventure\n"
                "4)Reports\n"
                "5)Exit",
                "Input Option: ",
                [1,2,3,4,5],["e","exit"]
                ))
        else:
            opc = int(mod.getOpt( \
                "1)Logout\n"
                "2)Play\n"
                "3)Replay Adventure\n"
                "4)Reports\n"
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
                idu = mod.get_table( \
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
            flg_sg = False
            flg_gopc = False
            aviable_adv = [0,]
            for i in mod.get_adventures_with_chars():
                aviable_adv.append(i)
            opcaj = mod.getOpt(mod.getFormatedAdventures(mod.get_adventures_with_chars()),"What adventure do you want to play?(0 Go back): ", aviable_adv,)
            if opcaj.isdigit():
                opcaj = int(opcaj)
                if opcaj == 0:
                    opc = 0
                else:
                    for i in aviable_adv[1:]:
                        if opcaj == i:
                            mod.game_context["idAdventure"] = opcaj
                            mod.game_context["nameAdventure"] = mod.get_adventures_with_chars()[i]["Name"]
                            flg_gopc = True
                        if flg_gopc:
                            break
                    if flg_gopc:
                            aviable_cha = [0,]
                            for i in mod.get_adventures_with_chars()[mod.game_context["idAdventure"]]["Characters"]:
                                aviable_cha.append(i)
                            cha_tab = ""
                            for i in mod.get_characters():
                                if i in aviable_cha:
                                    cha_tab += f"{i}) {mod.get_characters()[i]}\n"
                            opcha = mod.getOpt(cha_tab,"What character do you want to use?(0 Go back): ", aviable_cha,)
                            if opcha.isdigit():
                                opcha = int(opcha)
                                if opcha == 0:
                                    opc = 0
                                else:
                                    flg_copc = False
                                    for i in aviable_cha[1:]:
                                        if opcha == i:
                                            mod.game_context["idChar"] = opcha
                                            mod.game_context["characterName"] = mod.get_characters()[i]
                                            flg_copc = True
                                        if flg_copc:
                                            break
                                    if flg_copc:
                                        flg_sg = True
                                    else:
                                        print("This character id doesn't exist")
                            else: 
                                print("Only digit is valid")
                    else:
                        print("This adventure id doesn't exist")
            else: 
                print("Only digit is valid")
            if flg_sg: #Empieza el juego
                if mod.getIdGames() == []:
                    mod.game_context["idGame"] = 0
                else:
                    mod.game_context["idGame"] = mod.getIdGames()[-1]+1
                flg_cont = True
                print(mod.formatText(mod.get_id_bystep_adventure()[mod.get_first_step_adventure()]["Description"]),105,"/")
                stps = [[mod.get_first_step_adventure()]]
                stp = mod.get_first_step_adventure()
                while flg_cont:
                    ans = ""
                    for i in mod.get_id_bystep_adventure()[stp]["answers_in_step"]:
                        ans += mod.getFormatedAnswers(i,mod.get_answers_bystep_adventure()[(stp,i)]["Description"],105,4)+"\n"
                    dec = mod.getOpt(ans, "Que quieres hacer?",mod.get_id_bystep_adventure()[stp]["answers_in_step"],[])
                    stps[-1].append(dec)
                    stps.append([mod.get_answers_bystep_adventure()[(stp, dec)]["NextStep_Adventure"]])
                    stp = mod.get_answers_bystep_adventure()[(stp, dec)]["NextStep_Adventure"]
                    if mod.get_id_bystep_adventure()[stp]["Final_Step"] == 1:
                        flg_cont = False
                    print(mod.formatText(mod.get_id_bystep_adventure()[stp]["Description"],105,"/"))
                mod.insertCurrentGame(mod.game_context["idGame"],mod.game_context["idUser"],mod.game_context["idChar"],mod.game_context["idAdventure"])
                for step, answer in stps:
                    mod.insertCurrentChoice(mod.game_context["idGame"], step, answer)
                opt = 0
    elif opc == 3: #Replay Adventure
        rq = mod.get_table( \
            "SELECT 'Id', 'Username', 'Name', 'CharacterName', 'date' " \
            "UNION ALL " \
            "SELECT g.idGame, u.Username, adv.Name, c.CharacterName, g.Date " \
            "FROM game g " \
            "JOIN user u ON g.idUser = u.idUser " \
            "JOIN adventure adv ON g.idAdventure = adv.idAdventure " \
            "JOIN characters c ON g.idCharacter = c.idCharacter " \
            "ORDER BY g.Date DESC"
            )
        rg = mod.getOpt(mod.getFormatedTable(rq,"Partidas"),"Que partida quieres rejugar?: ",mod.getIdGames(),[])
        tr = mod.get_table(\
            "SELECT c.idByStep_Adventure, c.idAnswers_ByStep_Adventure "
            "FROM choices c "
            "WHERE c.idGame = %s "
            "ORDER BY c.idByStep_Adventure ASC" % (rg))
        mod.replay(tr)
        input("Press enter to continue...")
        opc = 0
    elif opc == 4: #Reports
        opcr = int(mod.getOpt( \
                "1)Most used answer\n"
                "2)Player with more games played\n"
                "3)Games played by user\n"
                "4)Back",
                "Input Option: ",
                [1,2,3,4],["","back"]
                ))
        if opcr == 1:
            answer = mod.get_table("""
                SELECT 'ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA - DESCRIPCION', 'NUMERO VECES SELECCIONADA'
                UNION ALL
                SELECT CONCAT(adv.idAdventure, ' - ', adv.Name), CONCAT(bs.idByStep_Adventure, ' - ', bs.Description), CONCAT(ans.idAnswers_ByStep_Adventure, ' - ', ans.Description), COUNT(c.idAnswers_ByStep_Adventure) AS 'NUMERO VECES SELECCIONADA'
                FROM answers_bystep_adventure ans
                JOIN bystep_adventure bs ON ans.idByStep_Adventure = bs.idByStep_Adventure
                JOIN adventure adv ON bs.idAdventure = adv.idAdventure
                LEFT JOIN choices c ON ans.idAnswers_ByStep_Adventure = c.idAnswers_ByStep_Adventure
                GROUP BY adv.idAdventure, adv.Name, bs.idByStep_Adventure, bs.Description, ans.idAnswers_ByStep_Adventure, ans.Description
                ORDER BY `NUMERO VECES SELECCIONADA` DESC
                """)
            print(mod.getFormatedTable(answer, "Most used answer"))
            input("Press enter to continue...")
        elif opcr == 2:
            answer = mod.get_table("""
                SELECT 'Nombre de usuario' AS username, 'Partidas Jugadas' AS partidas_jugadas
                UNION ALL
                SELECT Username, partidas_jugadas
                FROM (
                    SELECT u.Username AS Username, COUNT(g.idGame) AS partidas_jugadas
                    FROM `user` u
                    LEFT JOIN game g ON u.idUser = g.idUser
                    GROUP BY u.idUser
                    ORDER BY partidas_jugadas DESC
                    LIMIT 1
                ) AS t
                """)
            print(mod.getFormatedTable(answer, "Player with more games played"))
            input("Press enter to continue...")
        elif opcr == 3: 
            usr = input("De que usuario quieres ver las partidas?: ")
            answer = mod.get_table("""
                SELECT 'ID Aventura', 'Nombre Aventura', 'Fecha'
                UNION ALL
                SELECT idAventura, nombreAventura, fecha
                FROM (
                    SELECT adv.idAdventure AS idAventura,
                        adv.Name AS nombreAventura,
                        g.Date AS fecha
                    FROM `user` u
                    JOIN game g ON u.idUser = g.idUser
                    JOIN adventure adv ON g.idAdventure = adv.idAdventure
                    WHERE u.Username = '%s'
                    ORDER BY g.Date DESC
                ) AS t
            """ % usr)
            print(mod.getFormatedTable(answer, f"Games played by {usr}"))
            input("Press enter to continue...")
        elif opcr == 4:
            opc = 0
    elif opc == 5: #Salir
        print("Saliendo del juego")
        flgs = False