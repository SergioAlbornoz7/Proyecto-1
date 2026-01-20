###Librerias###

import datetime
import mysql.connector

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

adventures = { 
    # 1: {
    #     "Name": "nombre de la aventura id 1",
    #     "Description": "descripcion de la aventura id 1",
    #     "characters": [1,2] #lista con los ides de personajes id 1
    # }
}

characters = {
    # 1: "nombre el personaje id 1"
}

idAnswers_ByStep_Aventure = {
    # (1,3): { #(idAnswers_ByStep_Adventure, idByStep_Adventure)
    #     "Description": "descripcion del paso",
    #     "Resolution_answer": "Texto en el campo resolution answer BBDD",
    #     "NextStep_Adventure": 5 #Id del proximo paso
    # }
}

id_by_steps = {
    # 1: {
    #     "Description": "Descripcion del paso", 
    #     "answers_in_step": (1,2,3), #tupla  con los ids de las opciones en este paso
    #     "Final_Step": 0, #0 si no es un paso final 1 si si lo es
    #     }
}

replayAdventures = {
    # "idGame": {
    #     "idUser": 0,#id del usuario
    #     "Username": "Nombre del usuario",
    #     "idAdventure": 1, #id de la aventura
    #     "Name": "Nombre de la aventura",
    #     "date": datetime.datetime(2025,12,25,19,5,48), #fecha en formato datetime
    #     "idCharacter": 1, #id del personaje usado
    #     "CharacterName": "Nombre del personaje"
    #     }
}

###Funciones###

def get_answers_bystep_adventure(): #devuelve el diccionario answers_bystep_adventure
    if idAnswers_ByStep_Aventure:
        return idAnswers_ByStep_Aventure
    
def get_adventures_with_chars(): #devuelve el diccionario adventures
    return(adventures)

def get_id_bystep_adventure():
    dic = {}
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT idByStep_Adventure
        FROM bystep_adventure
        WHERE idAdventure = %s
        """, (game_context['idAdventure'],)
        )
    ids = tuple(row[0] for row in cursor.fetchall())
    for i in ids:
        dic[i] = id_by_steps[i]
    cursor.close()
    conexion.close()
    return(dic)

def get_first_step_adventure(): #Devuelve el primer paso de una aventura
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
    return characters

def getReplayAdventures(): #devuelve el diccionario replayAdventures
    return replayAdventures

def getChoices(): 
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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

def getIdGames(): #devuelve un diccionario con los ID de todas las partidas en la BBDD
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
    )
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT idGame
        FROM game
        """)
    result = tuple(row[0] for row in cursor.fetchall())
    cursor.close()
    conexion.close()
    return result

def insertCurrentGame(idGame,idUser,idChar,idAdventure): #guarda en la BBDD la partida actual
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
    )
    cursor = conexion.cursor()
    cursor.execute(query)
    result = tuple(cursor.fetchall())
    cursor.close()
    conexion.close()
    return result
def checkUserbdd(user,password): #Checkea un user y pswd en la BBDD 0 no existe,1 todo correcto, -1 contraseña incorrecta
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
        "Adventures".center(100,"=")+"\n\n"+\
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
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""): #Genera una cabecera de tabla
    total = 0
    for i in t_size_columns:
        total += i
    result = f"{title}".center(total,"=")+"\n"
    for i in range(len(t_name_columns)):
        result += f"{t_name_columns[i]}".ljust(t_size_columns[i])
    result += "\n" + "*"*total
    return result
def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data): #Genera una tabla en base a un diccionario
    result = ""
    for i in dict_of_data:
        for j in range(len(tuple_of_keys)):
            result += dict_of_data[i][tuple_of_keys[j]].ljust(weigth_of_columns[j])
        result += "\n"
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
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
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
    print("a") 