# Projet 1 - Bases de Données Réparties - 8INF803

## Equipe
* Mattys Gervais - GERM25050104
* Mathieu Dejeante - DEJM10010300
* Michael Morin - MORM07039500

## Sypnosis
La fédération française de football a décidé de mettre en place un système reparti. Le système est composé de cinq sites répartis dans le nord, l’est, l’ouest, le centre et le sud français afin de mieux répondre aux requêtes des clubs et des différents participants dans l’acte sportif. Dans ce mini-projet, nous cherchons à simuler le fonctionnement de la partie gestion des données de ce système, en utilisant le principe des Bases de Données réparties.

## Schemas Importants

### Base de Donnees
![Schema de la base de donnees et leurs relations](/BDD/schemas/BDD.png)

### Fragments et vues
![Schema des fragments et des vues materialisees selon la region](/BDD/schemas/schema%20bdd%20projet%20reparti%202.png)

### Solution Logicielle
![Schema de la solution logicielle en couche avec reference au MVC](/BDD/schemas/schema%20logiciel%20projet%20reparti.png)

# A Faire

## Base de Donnees
- [X] Schema - Tables
- [X] Schema - Fragments et Vues
- [X] SQL - Donnees de la BDD
- [X] SQL - Utilisateurs
- [X] SQL - Fragments
- [X] SQL - Drop tables centrales
- [ ] SQL - Vues 
- [ ] SQL - Vues materialisees

## Interface Utilisateur
- [X] Preparer - Arborescence
- [X] Preparer - Gitignore
- [X] Preparer - Licence
- [X] Preparer - Environment Virtuel
- [X] Preparer - Flask
- [X] Ecrire - Readme
- [X] Ecrire - Docker-compose
- [X] Ecrire - Requirements
- [X] Ecrire - Dockerfile
- [X] Main - Prepare app
- [X] Main - Debuter le serveur sur localhost:5000
- [X] Main - Ajouter config
- [X] Main - Ajouter Blueprints
- [X] Main - Ajouter LoginManager
- [X] Routes - Ajouter main
- [X] Routes - Ajouter common
- [X] Routes - Ajouter master
- [X] Controller - Definir main
- [X] Controller - Definir common
- [X] Controller - Definir master
- [X] DB_Abstraction - Definir engine
- [X] DB_Abstraction - Definir authentification
- [X] Obj_Abstraction - Definir User
- [X] Obj_Abstraction - Definir Club
- [X] Obj_Abstraction - Definir Stade
- [X] Obj_Abstraction - Definir Palmares
- [X] Obj_Abstraction - Definir Calendrier
- [X] Obj_Abstraction - Definir Match
- [X] Obj_Abstraction - Definir Bureau
- [X] Obj_Abstraction - Definir Arbitre
- [X] Obj_Abstraction - Definir StaffTechnique
- [X] Obj_Abstraction - Definir Equipe
- [X] Obj_Abstraction - Definir Joueur
- [X] Obj_Abstraction - Definir Personnel
- [X] Obj_Abstraction - Definir Dirigent
- [X] Obj_Implementation - Definir getUser
- [X] Obj_Implementation - Definir getList
- [X] Static - Ajouter le css de Bootstrap
- [X] Templates - Definir base.html
- [X] Templates - Definir login.html
- [X] Templates - Definir sidebar.html
- [X] Templates - Definir index.html

# Preparation de l'Environment 

## Necessaires de l'Environment
* Docker Desktop
* Python & Pip
* Bash ou PowerShell
* Modules Requis

## Environment Virtuel
Pour creer un environment virtuel, executer dans un terminal:
* `python -m venv ./env`
    * S'il n'y a pas de activate.bat ou de activate.ps1 dans /env/Scripts, executer la commande ci-dessus a nouveau.
*  `./env/Scripts/Activate.ps1` (PowerShell) ou `./env/Scripts/activate.bat` (Bash)

## Installer les Modules Requis
Executer dans un terminal:
* `python -m pip install --upgrade pip`
* `pip install -r ./UI/requirements.txt`

# Manuel d'Utilisateur

## Debuter la Solution Logicielle
Executer dans un terminal:
* `docker-compose build`
* `docker-compose up`

## Identifiants Disponibles
| Nom d'utilisateur | Mot de passe |
| :---: | :---: |
| system | (voir docker-compose.yml -> services - db - environment - ORACLE_PASSWORD) |
| b_master | b_master |
| b_region1 | b_region1 |
| b_region2 | b_region2 |
| b_region3 | b_region3 |
| b_region4 | b_region4 |

## Acceder a la base de donnees
* Verifier que le terminal a un message exprimant que la Base de donnees est prete
* Debuter SQLDevelopper
* Ajouter une connection avec un identifiant disponible et les parametres suivant:
    * URL: localhost
    * Port: 3223
    * Service: xe


## Acceder et Utiliser l'Interface Utilisateur
* Ouvrer un navigateur web
* Naviguer vers l'addresse localhost
* Vous etes rediriger vers la page Login
* Utiliser les identifiants disponibles pour vous connecter
* Le menu a gauche permet de selectionner un sujet a visualiser
* Le panneau de gauche liste les informations disponibles sur le sujet choisi ainsi que des boutons pour faire des modifications (Non implemente)
* Le sujet de la page d'accueil consiste en une liste detaillee des clubs de la region
