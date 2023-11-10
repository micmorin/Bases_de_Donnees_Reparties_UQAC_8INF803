from datetime import date, datetime
import re
from flask import flash
from flask_login import current_user
import ObjectAbstraction as obj
from DB_Abstraction import getSession, user_list
from sqlalchemy import select, text
from natsort import natsorted

def getUser(user, password):
    def createUserObj(tables):
        try:
            region = 1
            if 'ARBITRE' in tables : region = 0
            return obj.User(user,user,password,region,tables)
        except:
            return 0    
    
    def getAllMenuLinks():
        listOfList = []
        with getSession(user, password) as session:
            try:
                listObj = session.execute(text("SELECT OBJECT_NAME FROM USER_OBJECTS WHERE OBJECT_TYPE IN ('TABLE', 'VIEW')"))
                for o in listObj:
                    listOfList.append(o[0].lower())
            except:
                listOfList = []
        listOfList.sort()
        return listOfList
  
    table_list = getAllMenuLinks() 
    if len(table_list) == 0 : return 0
    user = createUserObj(table_list)
    user_list.append(user)
    return user
    
def getList(table, name, password):
    listOfList = []
    with getSession(name, password) as session:
            try:
                listObj = session.scalars(select(table)).all()
                for o in listObj:
                    listOfList.append(o.to_str())
                listOfList = natsorted(listOfList, key=lambda x: x[0])  
                listOfList.insert(0,listObj[0].getHeaders())
            except:
                listOfList = []
            return listOfList
    
def modifyObj(user, password, object, table):
    with getSession(user, password) as session:
        key = list(object.keys())[0]
        item = object[list(object.keys())[0]]
        all = session.scalars(select(table)).all()
        for a in all:
            if item == a.__dict__[key]:
                a.modifyFromList(list(object.values()))
        session.commit()
        return "Success"
    
def addObj(user, password, object, table):
    with getSession(user, password) as session:
        t = table()
        lastID = session.scalars(select(table)).all()[len(session.scalars(select(table)).all())-1].__dict__['MATCH']
        charID = "".join(re.findall("[a-zA-Z]", lastID))
        number = int("".join(re.findall("\d", lastID)))+1
        t.MATCH = charID + str(number)
        t.DATEMATCH = date.fromisoformat(list(object.values())[0])
        t.HEURE = datetime.fromisoformat(list(object.values())[1])
        t.CLUBA = list(object.values())[2]
        t.CLUBB = list(object.values())[3]
        t.STADE = list(object.values())[4]
        session.add(t)
        session.commit()
        return "Success"