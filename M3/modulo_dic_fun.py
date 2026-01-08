a = "borra esto luego"
###Librerias###

import datetime

###Diccionarios###

game_context = {
    "idGame": "",
    "idAdventure": "",
    "nameAdventure": "",
    "user": "",
    "idUser": "",
    "idChar": "",
    "characterName": ""
}

adventures = { 
    1: {
        "Name": "nombre de la aventura id 1",
        "Description": "descripcion de la aventura id 1",
        "characters": [1,2] #lista con los ides de personajes id 1
    }
}

characters = {
    1: "nombre el personaje id 1"
}

idAnswers_ByStep_Aventure = {
    ("idAnswer",)
}

id_by_steps = {
    1: {
        "Description": "Descripcion del paso", 
        "answers_in_step": (1,2,3), #tupla  con los ids de las opciones en este paso
        "Final_Step": 0, #0 si no es un paso final 1 si si lo es
        }
}

replayAdventures = {
    "idGame": {
        "idUser": 0,#id del usuario
        "Username": "Nombre del usuario",
        "idAdventure": 1, #id de la aventura
        "Name": "Nombre de la aventura",
        "date": datetime.datetime(2025,12,25,19,5,48), #fecha en formato datetime
        "idCharacter": 1, #id del personaje usado
        "CharacterName": "Nombre del personaje"
        }
}

###Funciones###

def get_answers_bystep_adventure():
    print(a)
def get_adventures_with_chars():
    print(a)
def get_id_bystep_adventure():
    print(a)
def get_first_step_adventure():
    print(a)
def get_characters():
    print(a)
def getReplayAdventures():
    print(a)
def getChoices():
    print(a)
def getIdGames():
    print(a)
def insertCurrentGame(idGame,idUser,isChar,idAdventure):
    print(a)
def getUsers():
    print(a)
def getUserIds():
    print(a)
def insertUser(id, user,password):
    print(a)
def get_table(query):
    print(a)
def checkUserbdd(user,password):
    print(a)
def setIdGame():
    print(a)
def insertCurrentChoice(idGame,actual_id_step,id_answer):
    print(a)
def formatText(text,lenLine,split):
    print(a)
def getHeader(text):
    print(a)
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    print(a)
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
