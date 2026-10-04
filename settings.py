from sqlalchemy.orm import sessionmaker , DeclarativeBase
from sqlalchemy import create_engine 
import os 
from dotenv import load_dotenv 

load_dotenv()

DATABASE_URL = str(os.getenv("DATABASE_URL"))

class Model(DeclarativeBase):
    pass 


engine = create_engine(
        DATABASE_URL ,
        echo = True 
)

sessionlocal = sessionmaker(
    bind=engine , autoflush=False 
)