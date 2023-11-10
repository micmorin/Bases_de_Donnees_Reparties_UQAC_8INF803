from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import ObjectAbstraction
Base = declarative_base()
user_list = []

def attemptConnection(user, password):
    with getSession(user, password) as session:
        try:
            statement = select(ObjectAbstraction.Table)
            user_obj = session.scalars(statement).all()
            return True
        except:
            return False

def getSession(user, password):
    engine = create_engine("oracle+oracledb://"+str(user)+":"+str(password)+"@bd:1521/xe")
    sessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return sessionFactory()