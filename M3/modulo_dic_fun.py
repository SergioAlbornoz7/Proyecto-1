a = 1
###Librerias###

import datetime
import mysql.connector

###Diccionarios###

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

def get_answers_bystep_adventure():
    if idAnswers_ByStep_Aventure:
        return idAnswers_ByStep_Aventure
    
def get_adventures_with_chars():
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
    list = tuple(row[0] for row in cursor.fetchall())
    for i in list:
        dic[i] = id_by_steps[i]
    cursor.close()
    conexion.close()
    return(dic)

def get_first_step_adventure():
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
        FROM id_by_steps
        WHERE idAdventure = %s
        """, (game_context['idAdventure'],)
        )
    result = cursor.fetchone()[0]
    cursor.close()
    conexion.close()
    return result

def get_characters():
    return characters

def getReplayAdventures():
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

def getIdGames():
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

def insertCurrentGame(idGame,idUser,idChar,idAdventure):
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

def getUsers():
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

def getUserIds():
    list = [[],[]]
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
        list[0].append(i[0])
        list[1].append(i[1])
    cursor.close()
    conexion.close()
    return list

def insertUser(id, user,password):
    conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Qwerty1_",
        database = "proyectomx"
    )
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT into user values (%s,%s,%s)
        """,(id,user,password)
        )
    conexion.commit()
    cursor.close()
    conexion.close()
def get_table(query):
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
def checkUserbdd(user,password):
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
    list = tuple(cursor.fetchall())
    if not list:
        return 0
    else:
        for i in list:
            if i[1] == password:
                return 1
        return -1

def setIdGame():
    print(a)
def insertCurrentChoice(idGame,actual_id_step,id_answer):
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
def formatText(text,lenLine,split):
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

def getHeader(text):
    return "*"*70+"/n"+ f"{text}".center(70,"=")+"/n"+"*"*70
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
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
                if lines[1] > tupla_sizes[1]:
                    result += " "*(tupla_sizes[1]-lines[1]+margin)
                    lines [1] = 0
                    for k in it3:
                        if lines[2] > tupla_sizes[2]:
                            result += "/n"
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
    
def getFormatedAdventures(adventures):
    desc = adventures["Description"].split()
    line = 0
    result = \
        "Adventures".center(100,"=")+"/n/n"+\
        "Id Adventure".ljust(14)+"Adventure".ljust(36)+"Description".ljust(50)+"/n"+\
        "*"*100+"/n"
    for i in adventures:
        result += f"{i}".ljust(14)+f"{i["Name"]}".ljust(36)
        for j in desc:
            if line > 0:
                if line + len(j) > 50:
                    result += "/n"+"".ljust(14)+"".ljust(36)+j+" "
                    line = len(j)+1
                else:
                    result += j + " "
                    line += len(j)+1
            else:
                result += j + " "
                line = len(j)+1
        result += "/n"
    return result

def getFormatedAnswers(idAnswer,text,lenLine,leftMargin):
    words = text.split()
    result = " "*leftMargin + f"{idAnswer})"
    line = len(f"{idAnswer})")
    for i in words:
        if line+len(i)+1 > lenLine:
            result += "/n" + " "*leftMargin + i
            line = len(i)
        else:
            result += f" {i}"
            line += len(f" {i}")
    return result
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    total = 0
    for i in t_size_columns:
        total += i
    result = f"{title}".center(total,"=")+"/n"
    for i in range(len(t_name_columns)):
        result += f"{t_name_columns[i]}".ljust(t_size_columns[i])
    result += "\n" + "*"*total
    return result
def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    result = ""
    for i in dict_of_data:
        for j in range(len(tuple_of_keys)):
            result += dict_of_data[i][tuple_of_keys[j]].ljust(weigth_of_columns[j])
        result += "/n"
    return result

def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    print (textOpts)
    opc = input(f"{inputOptText}")
    for i in rangeList:
        if opc == i:
            return opc
    for i in exceptions:
        if opc == i:
            return opc
    if dictionary:
        for i in dictionary:
            if opc == i:
                return opc
    else:
        print("Invalid option, select a valid one")
    
def getFormatedTable(queryTable,title=""):
    result = title.ljust()
def checkPassword(password):
    if len(password) in range(8,13):
        for i in range(len(password)):
            print(a)
def checkUser(user):
    if user.isalnum():
        return True
    else:
        print("user can only have alphanumeric characters")
        return False
def userExists(user):
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
        Where user = %s
        """,(user)
        )
    if cursor == "none":
        cursor.close()
        conexion.close()
        return False
    else:
        cursor.close()
        conexion.close()
        return True
def replay(choices):
    print(a)
