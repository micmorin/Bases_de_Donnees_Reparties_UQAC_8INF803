from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, Float
from sqlalchemy.orm import relationship
from datetime import date, datetime

from DB_Abstraction import Base, user_list

# -- AlphaSort PRIMARY TABLES: -------------------------------------------------------------------------------------------

class Bureau(Base):
    __tablename__ = "BUREAU"

    REGION = Column(String, primary_key=True, index=True)
    NOMBUREAU = Column(String, nullable=False)
    ADRESSE = Column(String)
    DATECREATION = Column(Integer)

    def to_str(self):
        return [self.REGION, self.NOMBUREAU, self.ADRESSE, self.DATECREATION]
    
    def getHeaders(self):
        return ['REGION', 'NOMBUREAU', 'ADRESSE', 'DATECREATION']

class Dirigeant(Base):
    __tablename__ = "DIRIGEANT"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String)
    PRENOM = Column(String)
    PROFESSION = Column(String)

    def to_str(self):
        return [self.CODE, self.NOM, self.PRENOM, self.PROFESSION]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'PRENOM', 'PROFESSION']

class Joueur(Base):
    __tablename__ = "JOUEUR"

    CODE = Column(Integer, primary_key=True, index=True)
    NOM = Column(String, index=True)
    PRENOM = Column(String)
    DATENAISSANCE = Column(Date)
    NATIONNALITE = Column(String)
    POIDS = Column(Integer)
    TAILLE = Column(Integer)
    CLASSE = Column(String)

    def to_str(self):
        return [self.CODE, self.NOM, self.PRENOM, self.DATENAISSANCE, self.NATIONNALITE, self.POIDS, self.TAILLE, self.CLASSE]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'PRENOM', 'DATENAISSANCE', 'NATIONNALITE', 'POIDS', 'TAILLE', 'CLASSE']
    
class Joueur_Global(Base):
    __tablename__ = "JOUEUR_GLOBAL"

    CODE = Column(Integer, primary_key=True, index=True)
    NOM = Column(String, primary_key=True, index=True)
    PRENOM = Column(String)
    DATENAISSANCE = Column(Date)
    NATIONNALITE = Column(String)
    POIDS = Column(Integer)
    TAILLE = Column(Integer)
    CLASSE = Column(String)

    def to_str(self):
        return [self.CODE, self.NOM, self.PRENOM, self.DATENAISSANCE, self.NATIONNALITE, self.POIDS, self.TAILLE, self.CLASSE]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'PRENOM', 'DATENAISSANCE', 'NATIONNALITE', 'POIDS', 'TAILLE', 'CLASSE']

# -- AlphaSort SECONDARY TABLES: -------------------------------------------------------------------------------------------

class Club(Base):
    __tablename__ = "CLUBSPORTIF"

    CODE = Column(String, primary_key=True, index=True)
    NOMCLUB = Column(String)
    DATECREATION = Column(Integer)
    DIRIGEANT = Column(String, ForeignKey('Dirigeant.CODE'))
    VILLE = Column(String)
    REGION = Column(String)

    def to_str(self):
        return [self.CODE, self.NOMCLUB, self.DATECREATION, self.DIRIGEANT, self.VILLE, self.REGION]
    
    def getHeaders(self):
        return ['CODE', 'NOMCLUB', 'DATECREATION', 'DIRIGEANT', 'VILLE', 'REGION']
    
class Club_Global(Base):
    __tablename__ = "CLUB_GLOBAL"

    CODE = Column(String, primary_key=True, index=True)
    NOMCLUB = Column(String)
    DATECREATION = Column(Integer)
    DIRIGEANT = Column(String, ForeignKey('Dirigeant.CODE'))
    VILLE = Column(String)
    REGION = Column(String)

    def to_str(self):
        return [self.CODE, self.NOMCLUB, self.DATECREATION, self.DIRIGEANT, self.VILLE, self.REGION]
    
    def getHeaders(self):
        return ['CODE', 'NOMCLUB', 'DATECREATION', 'DIRIGEANT', 'VILLE', 'REGION']

class Palmares(Base):
    __tablename__ = "PALMARES"

    CLUB = Column(String, ForeignKey('Club.CODE'), primary_key=True, index=True)
    ANNEE = Column(String, primary_key=True, index=True)
    TROPHEE = Column(String)
    NOMBREMATCHGAGNE = Column(Integer)
    NOMBREMATCHPERDUS = Column(Integer)

    def to_str(self):
        return [self.CLUB, self.ANNEE, self.TROPHEE, self.NOMBREMATCHGAGNE, self.NOMBREMATCHPERDUS]
    
    def getHeaders(self):
        return ['CLUB', 'ANNEE', 'TROPHEE', 'NOMBREMATCHGAGNE', 'NOMBREMATCHPERDUS']
    
class Palmares_Global(Base):
    __tablename__ = "PALMARES_GLOBAL"

    CLUB = Column(String, ForeignKey('Club.CODE'), primary_key=True, index=True)
    ANNEE = Column(String, primary_key=True, index=True)
    TROPHEE = Column(String)
    NOMBREMATCHGAGNE = Column(Integer)
    NOMBREMATCHPERDUS = Column(Integer)

    def to_str(self):
        return [self.CLUB, self.ANNEE, self.TROPHEE, self.NOMBREMATCHGAGNE, self.NOMBREMATCHPERDUS]
    
    def getHeaders(self):
        return ['CLUB', 'ANNEE', 'TROPHEE', 'NOMBREMATCHGAGNE', 'NOMBREMATCHPERDUS']
    
class Personnel(Base):
    __tablename__ = "PERSONNEL"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String, primary_key=True, index=True)
    PRENOM = Column(String)
    DATENAISSANCE = Column(Date)
    FONCTION = Column(String)
    REGION = Column(String, ForeignKey('Bureau.REGION'))
    VILLE = Column(String)

    def to_str(self):
        return [self.CODE, self.NOM, self.PRENOM, self.DATENAISSANCE, self.FONCTION, self.REGION, self.VILLE]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'PRENOM', 'DATENAISSANCE', 'FONCTION', 'REGION', 'VILLE']

class Personnel_Global(Base):
    __tablename__ = "PERSONNEL_GLOBAL"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String, primary_key=True, index=True)
    PRENOM = Column(String)
    DATENAISSANCE = Column(Date)
    FONCTION = Column(String)
    REGION = Column(String, ForeignKey('Bureau.REGION'))
    VILLE = Column(String)

    def to_str(self):
        return [self.CODE, self.NOM, self.PRENOM, self.DATENAISSANCE, self.FONCTION, self.REGION, self.VILLE]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'PRENOM', 'DATENAISSANCE', 'FONCTION', 'REGION', 'VILLE']

class Stade(Base):
    __tablename__ = "STADE"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String)
    VILLE = Column(String)
    REGION = Column(String, ForeignKey('Bureau.REGION'))
    CAPACITE = Column(Integer)

    def to_str(self):
        return [self.CODE, self.NOM, self.VILLE, self.REGION, self.CAPACITE]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'VILLE', 'REGION', 'CAPACITE']
    
class Stade_Global(Base):
    __tablename__ = "STADE_GLOBAL"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String)
    VILLE = Column(String)
    REGION = Column(String, ForeignKey('Bureau.REGION'))
    CAPACITE = Column(Integer)

    def to_str(self):
        return [self.CODE, self.NOM, self.VILLE, self.REGION, self.CAPACITE]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'VILLE', 'REGION', 'CAPACITE']
    
class Stafftechnique(Base):
    __tablename__ = "STAFFTECHNIQUE"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String)
    CLUB = Column(String, ForeignKey('Club.CODE'))
    FONCTION = Column(String)

    def to_str(self):
        return [self.CODE, self.NOM, self.CLUB, self.FONCTION]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'CLUB', 'FONCTION']
    
class Staff_technique_Global(Base):
    __tablename__ = "STAFF_TECHNIQUE_GLOBAL"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String)
    CLUB = Column(String, ForeignKey('Club.CODE'))
    FONCTION = Column(String)

    def to_str(self):
        return [self.CODE, self.NOM, self.CLUB, self.FONCTION]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'CLUB', 'FONCTION']

# -- AlphaSort TERITARY TABLES: -------------------------------------------------------------------------------------------

class Arbitre(Base):
    __tablename__ = "ARBITRE"

    CODE = Column(String, primary_key=True, index=True)
    NOM = Column(String)
    PRENOM = Column(String)
    DATENAISSANCE = Column(Date)
    REGION = Column(String, ForeignKey('Bureau.REGION'))
    CLUBPREFERE = Column(String, ForeignKey('Club.CODE'))

    def to_str(self):
        return [self.CODE, self.NOM, self.PRENOM, self.DATENAISSANCE, self.REGION, self.CLUBPREFERE]
    
    def getHeaders(self):
        return ['CODE', 'NOM', 'PRENOM', 'DATENAISSANCE', 'REGION', 'CLUBPREFERE']

class Equipe(Base):
    __tablename__ = "EQUIPE"

    CLUB = Column(String, ForeignKey('Club.CODE'), primary_key=True, index=True)
    JOUEUR = Column(Integer, ForeignKey('Joueur.CODE'), primary_key=True, index=True)
    DATEDEBUTCONTRAT = Column(Date)
    DATEFINCONTRAT = Column(Date)
    NUMEROMAILLOT = Column(Integer)
    POSTE = Column(String)

    def to_str(self):
        return [self.CLUB, self.JOUEUR, self.DATEDEBUTCONTRAT, self.DATEFINCONTRAT, self.NUMEROMAILLOT, self.POSTE]
    
    def getHeaders(self):
        return ['CLUB', 'JOUEUR', 'DATEDEBUTCONTRAT', 'DATEFINCONTRAT', 'NUMEROMAILLOT', 'POSTE']
    
class Match(Base):
    __tablename__ = "MATCH"

    CODE = Column(String, primary_key=True, index=True)
    NBREBUTCLUBA = Column(Integer)
    NBREBUTCLUBB = Column(Integer)
    NBRESPECTATEURS = Column(Integer)
    ARBITRE = Column(String, ForeignKey('Arbitre.CODE'))
    STADE = Column(String,ForeignKey('Stade.CODE'))

    def to_str(self):
        return [self.CODE, self.NBREBUTCLUBA, self.NBREBUTCLUBB, self.NBRESPECTATEURS, self.ARBITRE, self.STADE]
    
    def getHeaders(self):
        return ['CODE', 'NBREBUTCLUBA', 'NBREBUTCLUBB', 'NBRESPECTATEURS', 'ARBITRE', 'STADE']    
    
class Match_Global(Base):
    __tablename__ = "MATCH_GLOBAL"

    CODE = Column(String, primary_key=True, index=True)
    NBREBUTCLUBA = Column(Integer)
    NBREBUTCLUBB = Column(Integer)
    NBRESPECTATEURS = Column(Integer)
    ARBITRE = Column(String, ForeignKey('Arbitre.CODE'))
    STADE = Column(String,ForeignKey('Stade.CODE'))

    def to_str(self):
        return [self.CODE, self.NBREBUTCLUBA, self.NBREBUTCLUBB, self.NBRESPECTATEURS, self.ARBITRE, self.STADE]
    
    def getHeaders(self):
        return ['CODE', 'NBREBUTCLUBA', 'NBREBUTCLUBB', 'NBRESPECTATEURS', 'ARBITRE', 'STADE']   

# -- AlphaSort QUADIARY TABLES: -------------------------------------------------------------------------------------------

class Calendrier(Base):
    __tablename__ = "CALENDRIER"

    MATCH = Column(String, ForeignKey('Match.CODE'), primary_key=True, index=True)
    DATEMATCH = Column(Date, primary_key=True, index=True)
    HEURE = Column(Time)
    CLUBA = Column(String, ForeignKey('Club.CODE'))
    CLUBB = Column(String, ForeignKey('Club.CODE'))
    STADE = Column(String, ForeignKey('Stade.CODE'))

    def to_str(self):
        return [self.MATCH, self.DATEMATCH, self.HEURE, self.CLUBA, self.CLUBB, self.STADE]
    
    def getHeaders(self):
        return ['MATCH', 'DATEMATCH', 'HEURE', 'CLUBA', 'CLUBB', 'STADE']
    
class Calendrier_Global(Base):
    __tablename__ = "CALENDRIER_GLOBAL"

    MATCH = Column(String, primary_key=True, index=True)
    DATEMATCH = Column(Date, primary_key=True, index=True)
    HEURE = Column(Time)
    CLUBA = Column(String)
    CLUBB = Column(String)
    STADE = Column(String)

    def to_str(self):
        return [self.MATCH, self.DATEMATCH, self.HEURE, self.CLUBA, self.CLUBB, self.STADE]
    
    def getHeaders(self):
        return ['MATCH', 'DATEMATCH', 'HEURE', 'CLUBA', 'CLUBB', 'STADE']
    
    def modifyFromList(self, list):
        self.MATCH = list[0]
        self.DATEMATCH = date.fromisoformat(list[1])
        self.HEURE = datetime.fromisoformat(list[2])
        self.CLUBA =list[3]
        self.CLUBB = list[4]
        self.STADE = list[5]
    
class Statistiquebuts(Base):
    __tablename__ = "STATISTIQUE_BUTS"

    REGION = Column(String, primary_key=True, index=True)
    CLUB = Column(String, primary_key=True, index=True)
    BUTS_MARQUES = Column(Integer)

    def to_str(self):
        return [self.REGION, self.CLUB, self.BUTS_MARQUES]
    
    def getHeaders(self):
        return ['REGION', 'CLUB', 'BUTS_MARQUES']
    
class Statistiquepalmares(Base):
    __tablename__ = "STATISTIQUE_PALMARES"

    GAGNANT = Column(String, primary_key=True, index=True)
    NB_MATCH_GAGNE = Column(Integer)

    def to_str(self):
        return [self.GAGNANT, self.NB_MATCH_GAGNE]
    
    def getHeaders(self):
        return ['GAGNANT', 'NB_MATCH_GAGNE']
    
class Statistiqueresultatmatch(Base):
    __tablename__ = "STATISTIQUE_RESULTAT_MATCH"

    CODE = Column(String, primary_key=True, index=True)
    GAGNANT = Column(String)

    def to_str(self):
        return [self.CODE, self.GAGNANT]
    
    def getHeaders(self):
        return ['CODE', 'GAGNANT']
    
class Statistiquespectateur(Base):
    __tablename__ = "STATISTIQUE_SPECTATEUR"

    REGION = Column(String, primary_key=True, index=True)
    TOTAL_SPECTATEURS = Column(Float)

    def to_str(self):
        return [self.REGION, self.TOTAL_SPECTATEURS]
    
    def getHeaders(self):
        return ['REGION', 'TOTAL_SPECTATEURS']

# -- AlphaSort UTILITIES TABLES: -------------------------------------------------------------------------------------------

class Table(Base):
    __tablename__ = "user_tables"

    table_name = Column(String, primary_key=True)

    def to_str(self):
        return self.table_name.lower()
    
    def getHeaders(self):
        return ''

class User():
    def __init__(self, id, name, password, region_id, tables):
        self.id = id
        self.name = name
        self.password = password
        self.region_id = region_id
        self.tables = tables

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)    

    def get(id):
        for user in user_list:
            if user.id == id: return user
        return None