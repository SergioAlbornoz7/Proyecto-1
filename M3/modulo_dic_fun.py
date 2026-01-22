###Librerias###

import datetime
import mysql.connector
import textwrap

###SQL Config###

hostq = "localhost"
portq = 3306
userq = "root"
passwordq = "Qwerty1_"
databaseq = "proyectomx"

###Funciones###

def get_answers_bystep_adventure(): #devuelve el diccionario answers_bystep_adventure
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
        )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT idAnswers_ByStep_Adventure, idByStep_Adventure, Description, Resolution_Anwer, NextStep_Adventure
        FROM answers_bystep_adventure
        """)
    raw = cursor.fetchall()
    cursor.close()
    conexion.close()
    idAnswers_ByStep_Aventure = {}
    for i in raw:
        key = (i["idAnswers_ByStep_Adventure"], i["idByStep_Adventure"])
        idAnswers_ByStep_Aventure[key] = {
            "Description": i["Description"],
            "Resolution_answer": i["Resolution_Anwer"],
            "NextStep_Adventure": i["NextStep_Adventure"]
            }
    return idAnswers_ByStep_Aventure
def get_adventures_with_chars(): #devuelve el diccionario adventures
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT idAdventure, Name, Description
        FROM adventure
        """)
    aventuras_raw = cursor.fetchall()
    cursor.execute("""
        SELECT a.idAdventure, c.idCharacter 
        FROM adventure a 
        JOIN characters c ON c.idCharacter = a.idCharacter 
        """)
    chars_raw = cursor.fetchall()
    cursor.close()
    conexion.close()
    aventuras = {}
    for i in aventuras_raw:
        aventuras[i["idAdventure"]] = {
            "Name": i["Name"],
            "Description": i["Description"],
            "Characters": []
            }
    for i in chars_raw:
        aventuras[i["idAdventure"]]["Characters"].append(i["idCharacter"])
    return(aventuras)
def get_id_bystep_adventure():
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(f"""
        SELECT idByStep_Adventure, Description, Final_Step
        FROM bystep_adventure
        WHERE idAdventure = {game_context['idAdventure']}
        """)
    steps_raw = cursor.fetchall()
    cursor.execute(f"""
        SELECT idByStep_Adventure, idAnswers_ByStep_Adventure
        FROM answers_bystep_adventure
        WHERE idAdventure = {game_context['idAdventure']}
        """)
    answers_raw = cursor.fetchall()
    cursor.close()
    conexion.close()
    id_by_steps = {}
    for i in steps_raw:
        id_by_steps[i["idByStep_Adventure"]] = {
            "Description": i["Description"],
            "answers_in_step": [],
            "Final_Step": i["Final_Step"]
            }
    for i in answers_raw:
        id_by_steps[i["idByStep_Adventure"]]["answers_in_step"].append(
            i["idAnswers_ByStep_Adventure"]
            )
    for i in id_by_steps:
        id_by_steps[i]["answers_in_step"] = tuple(id_by_steps[i]["answers_in_step"])
    return id_by_steps
def get_first_step_adventure(): #Devuelve el primer paso de una aventura
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT MIN(idByStep_Adventure)
        FROM bystep_adventure
        WHERE idAdventure = %s
        """, (game_context['idAdventure'],)
        )
    result = cursor.fetchone()[0]
    cursor.close()
    conexion.close()
    return result
def get_characters(): #devuelve el diccionario characters
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT idCharacter, CharacterName
        FROM characters
        """)
    raw = cursor.fetchall()
    personajes = {}
    for i in raw:
        personajes[i["idCharacter"]] = i["CharacterName"]
    return(personajes)

def getReplayAdventures(): #devuelve el diccionario replayAdventures
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT g.idGame, g.idUser, u.Username, g.idAdventure, a.Name,g.Date, g.idCharacter, c.CharacterName
        FROM game g
        JOIN user u ON u.idUser = g.idUser
        JOIN adventure a ON a.idAdventure = g.idAdventure
        JOIN characters c ON c.idCharacter = g.idCharacter
        """)
    raw = cursor.fetchall()
    cursor.close()
    conexion.close()
    replayAdventures = {}
    for i in raw:
        replayAdventures[i["idGame"]] = {
            "idUser": i["idUser"],
            "Username": i["Username"],
            "idAdventure": i["idAdventure"],
            "Name": i["Name"],
            "date": i["Date"],
            "idCharacter": i["idCharacter"],
            "CharacterName": i["CharacterName"]
            }
    return replayAdventures
def getChoices(): 
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT idByStep_Adventure, idAnswers_ByStep_Adventure
        From choices
        WHERE idGame = %s
        """, (game_context['idGame'],)
        )
    result = tuple(cursor.fetchall())
    cursor.close()
    conexion.close()
    return result

def getIdGames(): #devuelve una tupla con los ID de todas las partidas en la BBDD
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT idGame
        FROM game
        """)
    result = tuple(i[0] for i in cursor.fetchall())
    cursor.close()
    conexion.close()
    return result

def insertCurrentGame(idGame,idUser,idChar,idAdventure): #guarda en la BBDD la partida actual
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT into game values (%s,%s,%s,%s,%s)
        """,(idGame,idUser,idChar,idAdventure,datetime.datetime.now())
        )
    conexion.commit()
    cursor.close()
    conexion.close()

def getUsers(): #devuelve un diccionario con toda la tabla de users de la BBDD
    dic = {}
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT Username, Password, idUser
        FROM user
        """)
    for i in tuple(cursor.fetchall()):
        dic[i[0]] = {"password":i[1],"idUser":i[2]}
    cursor.close()
    conexion.close()
    return dic

def getUserIds(): #devuelve Una lista con los ID y el Username
    ides = [[],[]]
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT Username,idUser
        FROM user
        """)
    for i in tuple(cursor.fetchall()):
        ides[0].append(i[0])
        ides[1].append(i[1])
    cursor.close()
    conexion.close()
    return ides

def insertUser(id, user,password): #Crea un nuevo usuario en la BBDD
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute(f"""
        INSERT into user values ({id},%s,%s)
        """,(user,password)
        )
    conexion.commit()
    cursor.close()
    conexion.close()
def get_table(query): #Permite hacer cualquier Query a la BBDD
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute(query)
    result = tuple(cursor.fetchall())
    cursor.close()
    conexion.close()
    return result
def checkUserbdd(user,password): #Checkea un user y pswd en la BBDD 0 no existe,1 todo correcto, -1 contraseña incorrecta
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT Username, Password
        FROM user
        WHERE Username = %s
        """, (user,)
        )
    uspsw = tuple(cursor.fetchall())
    if not uspsw:
        return 0
    else:
        for i in uspsw:
            if i[1] == password:
                return 1
        return -1

def setIdGame(): #Crea una nueva partida en la BBDD
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT into game values (NULL,%s,%s,%s,%s)
        """,(game_context["idUser"],game_context["idChar"],game_context["idAdventure"],datetime.datetime.now())
        )
    conexion.commit()
    cursor.close()
    conexion.close()
def insertCurrentChoice(idGame,actual_id_step,id_answer): #Inserta en la BBDD la decision tomada por el jugador
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT into choices values (%s,%s,%s)
        """,(idGame,actual_id_step,id_answer)
        )
    conexion.commit()
    cursor.close()
    conexion.close()
def formatText(text,lenLine,split): #Formatea texto
    words = text.split()
    lines = []
    current = ""
    for i in words:
        if len(current) + len(i) + 1 > lenLine:
            lines.append(current)
            current = i
        else:
            if current:
                current += f" {i}"
            else:
                current = i
    if current:
        lines.append(current)
    return split.join(lines)

def getHeader(text): #Formatea cabecera
    return "*"*70+"\n"+ f"{text}".center(70,"=")+"\n"+"*"*70
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0): #Formatea tres textos en tres columnas
    it1 = iter(tupla_texts[0].split())
    it2 = iter(tupla_texts[1].split())
    it3 = iter(tupla_texts[2].split())
    lines = [0,0,0]
    result = ""
    for i in it1:
        if lines[0]+len(i)+1 > tupla_sizes[0]:
            result += " "*(tupla_sizes[0]-lines[0]+margin)
            lines [1] = 0
            for j in it2:
                if lines[1] + len(j) + 1 > tupla_sizes[1]:
                    result += " "*(tupla_sizes[1]-lines[1]+margin)
                    lines [1] = 0
                    for k in it3:
                        if lines[2] + len(k) + 1 > tupla_sizes[2]:
                            result += "\n"
                            lines[2] = 0
                            break
                        elif lines[2] == 0:
                            result += k
                            lines[2] += len(k)
                        else:
                            result += " "+k
                            lines[2] += len(k)+1
                    break
                elif lines[1] == 0:
                    result += j
                    lines[1] += len(j)
                else:
                    result += " "+j
                    lines[1] += len(j)+1
        elif lines[0] == 0:
            result += i
            lines[0] += len(i)
        else:
            result += " "+i
            lines[0] += len(i)+1
    return result
    
def getFormatedAdventures(adventures): #Devuelve un string con el diccionario adventures formateado como tabla
    result = \
        "Adventures".center(100,"=")+"\n"+\
        "Id Adventure".ljust(14)+"Adventure".ljust(36)+"Description".ljust(50)+"\n"+\
        "*"*100+"\n"
    for i in adventures:
        line = 0
        desc = adventures[i]["Description"].split()
        result += f"{i}".ljust(14)+f"{adventures[i]["Name"]}".ljust(36)
        for j in desc:
            if line > 0:
                if line + len(j) > 50:
                    result += "\n"+"".ljust(14)+"".ljust(36)+j+" "
                    line = len(j)+1
                else:
                    result += j + " "
                    line += len(j)+1
            else:
                result += j + " "
                line = len(j)+1
        result += "\n"
    return result

def getFormatedAnswers(idAnswer,text,lenLine,leftMargin): #Formatea las decisiones en un paso
    words = text.split()
    result = " "*leftMargin + f"{idAnswer})"
    line = len(f"{idAnswer})")
    for i in words:
        if line+len(i)+1 > lenLine:
            result += "\n" + " "*leftMargin + i
            line = len(i)
        else:
            result += f" {i}"
            line += len(f" {i}")
    return result
def getHeaderForTableFromTuples(t_name_columns,t_size_columns,title=""): #Genera una cabecera de tabla
    total = 0
    for i in t_size_columns:
        total += i
    result = f"{title}".center(total,"=")+"\n"
    for i in range(len(t_name_columns)):
        result += f"{t_name_columns[i]}".ljust(t_size_columns[i])
    result += "\n" + "*"*total
    return result
def getTableFromDict(tuple_of_keys, weigth_of_columns, dict_of_data):
    result = ""
    for i in dict_of_data:
        wrapped_columns = []
        wrapped_key = textwrap.wrap(str(i), weigth_of_columns[0]) or [""]
        wrapped_columns.append(wrapped_key)
        for j in range(len(tuple_of_keys)):
            text = str(dict_of_data[i][tuple_of_keys[j]])
            wrapped = textwrap.wrap(text, weigth_of_columns[j+1]) or [""]
            wrapped_columns.append(wrapped)
        max_lines = max(len(col) for col in wrapped_columns)
        for line in range(max_lines):
            row = ""
            for col_index, col in enumerate(wrapped_columns):
                if line < len(col):
                    row += col[line].ljust(weigth_of_columns[col_index])
                else:
                    row += "".ljust(weigth_of_columns[col_index])
            result += row + "\n"
    return result
def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[]): #Genera un menu
    while True:
        print (textOpts)
        opc = input(f"{inputOptText}")
        for i in rangeList:
            if opc == str(i):
                return opc
        for i in exceptions:
            if opc == i:
                return rangeList[-1]
        else:
            print("Invalid option, select a valid one")
    
def getFormatedTable(queryTable,title=""): #Genera una tabla en base a una tupla
    columns = len(queryTable[0])
    wide = (120 // columns)
    result = title.center(120, "=") + "\n"
    for head in queryTable[0]:
        result += (str(head) + " ").ljust(wide)
    result += "\n" + "*" * 120 + "\n\n"
    for i in range(1, len(queryTable)):
        palabras = [str(cell or "").split() for cell in queryTable[i]]
        sp_iter = [iter(p) for p in palabras]
        pending = [None] * columns
        check = [len(p) > 0 for p in palabras]
        while any(check):
            linea_fila = ""
            for k in range(columns):
                if not check[k]:
                    linea_fila += "".ljust(wide)
                    continue
                palabra = pending[k]
                pending[k] = None
                if palabra is None:
                    try:
                        palabra = next(sp_iter[k])
                    except StopIteration:
                        check[k] = False
                        linea_fila += "".ljust(wide)
                        continue
                linea_celda = ""
                while palabra:
                    limite = wide - 1
                    if len(palabra) > limite and not linea_celda:
                        linea_celda = palabra[:limite - 1] + "…"
                        palabra = None
                        break
                    espacio = 1 if linea_celda else 0
                    if len(linea_celda) + espacio + len(palabra) <= limite:
                        linea_celda += (" " if linea_celda else "") + palabra
                        try:
                            palabra = next(sp_iter[k])
                        except StopIteration:
                            check[k] = False
                            palabra = None
                    else:
                        pending[k] = palabra
                        palabra = None
                linea_fila += (linea_celda + " ").ljust(wide)
            result += linea_fila + "\n"
        result += "\n"
    return result
def checkPassword(password): #Chekea si una contraseña es segura
    flg_may = False
    flg_min = False
    flg_num = False
    flg_cha = False
    if len(password) in range(8,13):
        for i in range(len(password)):
            if password[i].isupper():
                flg_may = True
            elif password[i].islower():
                flg_min = True
            elif password[i].isdigit():
                flg_num = True
            else:
                flg_cha = True
        if flg_min and flg_may and flg_cha and flg_num:
            return True
        else:
            print("Invalid password")
            return False
    else:
        print("Invalid password")
        return False
def checkUser(user): #Chekea si un usuario es valido
    if user.isalnum():
        if len(user) < 10:
            if len(user) >= 6:
                return True
            else:
                print("User too short min 6 characters")
        else:
            print("User too long max 10 characters")
    else:
        print("user can only have alphanumeric characters")
        return False
def userExists(user): #Chekea si un usuario ya existe en la BBDD
    conexion = mysql.connector.connect(
        host = hostq,
        port = portq,
        user = userq,
        password = passwordq,
        database = databaseq
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT Username
        From user
        Where Username = %s
        """,(user,)
        )
    exists = cursor.fetchone() is not None
    cursor.close()
    conexion.close()
    return exists
def replay(choices):
    for i in choices:
        print(formatText(get_id_bystep_adventure()[choices[i][0]]["Description"]),105,"/")
        ans = ""
        for j in get_id_bystep_adventure()[i[0]]["answers_in_step"]:
            ans += getFormatedAnswers(j,get_answers_bystep_adventure()[(i[0],j)]["Description"],105,4)+"\n"
            print(ans)
        input("Press enter to continue...")

###Diccionarios###

yes = ["y","s","yes","si"]

game_context = {
    "idGame": "", #digit
    "idAdventure": "", #digit
    "nameAdventure": "",
    "user": "",
    "idUser": "", #digit
    "idChar": "", #digit
    "characterName": ""
}

#adventures = get_adventures_with_chars()
    # 1: {
    #     "Name": "nombre de la aventura id 1",
    #     "Description": "descripcion de la aventura id 1",
    #     "Characters": [1,2] #lista con los ides de personajes id 1
    # }

#characters = get_characters()
    # 1: "nombre el personaje id 1"
#idAnswers_ByStep_Aventure = get_answers_bystep_adventure()
    # (1,3): { #(idAnswers_ByStep_Adventure, idByStep_Adventure)
    #     "Description": "descripcion del paso",
    #     "Resolution_answer": "Texto en el campo resolution answer BBDD",
    #     "NextStep_Adventure": 5 #Id del proximo paso
    # }
#id_by_steps = get_id_bystep_adventure()
    # 1: {
    #     "Description": "Descripcion del paso", 
    #     "answers_in_step": (1,2,3), #tupla  con los ids de las opciones en este paso
    #     "Final_Step": 0, #0 si no es un paso final 1 si si lo es
    #     }
#replayAdventures = getReplayAdventures()
    # "idGame": {
    #     "idUser": 0,#id del usuario
    #     "Username": "Nombre del usuario",
    #     "idAdventure": 1, #id de la aventura
    #     "Name": "Nombre de la aventura",
    #     "date": datetime.datetime(2025,12,25,19,5,48), #fecha en formato datetime
    #     "idCharacter": 1, #id del personaje usado
    #     "CharacterName": "Nombre del personaje"
    #     }
 