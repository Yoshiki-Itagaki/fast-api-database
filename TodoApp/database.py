from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from .env_local import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST

load_dotenv()

# SQLite3
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# PostgreSQL
DB_USER = DB_USER
DB_PASSWORD = DB_PASSWORD
DB_HOST = DB_HOST
DB_NAME = DB_NAME

SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# MySQL
# pw = ''
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:@127.0.0.1:3306/TodoApplicationDatabase'

# SQLite3
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# PostgreSQL & MySQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
