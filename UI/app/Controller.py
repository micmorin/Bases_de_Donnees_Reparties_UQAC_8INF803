from flask import render_template, request, redirect, url_for, flash
from flask_login import  login_required, login_user, logout_user, current_user
import ObjectImplementation as obj
import DB_Abstraction as db


def getMenuLinks():
    tables = []
    for table in current_user.tables:
        try:
            u = url_for('user.'+table)
            tables.append(table)
        except:
            continue # MAKE ADD and MODIFY BUTTON WORK
    return tables

"""
------------
MAIN ROUTES
------------
"""

def main_index():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Club, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

def main_login():
    if request.method == 'POST':      
            if db.attemptConnection(request.form['username'], request.form['password']):
                user = obj.getUser(request.form['username'], request.form['password'])
                if not isinstance(user,obj.obj.User): flash("Unable to create user with Username/Password. Try Again.")
                else:
                    login_user(user)
                    return redirect(url_for('main.main_index'))
            else:
                flash("Unable to connect with Username/Password. Try Again.")
        
    return render_template("login.html")

@login_required
def main_logout():
    logout_user()
    return redirect(url_for('main.main_login'))

"""
------------
COMMON ROUTES
------------
"""

@login_required
def personnel():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Personnel, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def palmares():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Palmares, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def calendrier():
    if current_user.is_authenticated:
        if request.method == 'POST':
            if len(request.form) == 6:
                flash(obj.modifyObj(current_user.name, current_user.password, dict(request.form), obj.obj.Calendrier_Global))
            else:
               flash(obj.addObj(current_user.name, current_user.password, dict(request.form), obj.obj.Calendrier_Global)) 
        listObj = obj.getList(obj.obj.Calendrier, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def match():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Match, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def stafftechnique():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Stafftechnique, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def equipe():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Equipe, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def joueur():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Joueur, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def stade():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Stade, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

"""
------------
MASTER ROUTES
------------
"""

@login_required
def bureau():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Bureau, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[] 
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def arbitre():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Arbitre, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def dirigeant():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Dirigeant, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def statistique_spectateur():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Statistiquespectateur, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def statistique_buts():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Statistiquebuts, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def statistique_resultat_match():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Statistiqueresultatmatch, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def statistique_palmares():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Statistiquepalmares, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

"""
------------
GLOBAL ROUTES
------------
"""

@login_required
def palmares_Global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Palmares_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def calendrier_Global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Calendrier_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def club_global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Club_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def joueur_global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Joueur_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def match_global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Match_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def personnel_global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Personnel_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def staff_technique_global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Staff_technique_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))

@login_required
def stade_global():
    if current_user.is_authenticated:
        listObj = obj.getList(obj.obj.Stade_Global, current_user.name, current_user.password)
        if len(listObj) != 0 : titles = listObj.pop(0) 
        else: titles=[]
        return render_template("index.html", tables=getMenuLinks(), listObj=listObj, titles=titles)
    return redirect(url_for('main.main_login'))