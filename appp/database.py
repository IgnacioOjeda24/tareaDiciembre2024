#These are the libraries to configure the database and declare the base for the models.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#The location or address where the SQL Alchemy database connection will go.
DATABASE_URL = 'sqlite:///data/tareas.db'
#The database is configured here.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
# Base declaration for models.
Base = declarative_base()
