from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
import os
from dotenv import load_dotenv
load_dotenv()

MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_ROOT_PASSWORD= os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_USER= os.getenv("MYSQL_USER")
MYSQL_PASSWORD= os.getenv("MYSQL_PASSWORD")
MYSQL_HOST=os.getenv("MYSQL_HOST")
MYSQL_PORT=os.getenv("MYSQL_PORT")

DATABASE_URL = (f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}")

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]