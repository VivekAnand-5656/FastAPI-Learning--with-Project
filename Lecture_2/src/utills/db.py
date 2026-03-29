from sqlalchemy import create_engine                # create connection from database
from sqlalchemy.orm import sessionmaker, declarative_base           # sessionmaker create db session for run queries , base class for to be make models
from src.utills.settings import setting

Base = declarative_base()               # most important
engine = create_engine(url=setting.DB_CONNECTION)   # create engine
LocalSession = sessionmaker(bind=engine)      # temporary conversation with DB

#====== FastAPI Dependency 
def get_db():
    session = LocalSession()  #connection open
    try:
        yield session     # give session to api function
    finally:
        session.close()     # close DB connecition