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
    words = [tupla_texts[0].split(),tupla_texts[1].split(),tupla_texts[2].split()]
    lines = [[],[],[]]
    current = ["","",""]
    return
    
def getFormatedAdventures(adventures):
    print(a)
def getFormatedAnswers(idAnswer,text,lenLine,leftMargin):
    print(a)
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    print(a)
def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    print(a)
def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    print(a)
def getFormatedTable(queryTable,title=""):
    print(a)
def checkPassword(password):
    print(a)
def checkUser(user):
    print(a)
def userExists(user):
    print(a)
def replay(choices):
    print(a)
