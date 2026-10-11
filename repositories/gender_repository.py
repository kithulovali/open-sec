from models.utils import Gender 
from sqlalchemy.orm import Session 
from sqlalchemy import select 

class GenderRepository :
    
    def __init__(self , session : Session) :
        self.session = session 
        
        
    def get_by_name(self,name:str) -> Gender | None :
        statement = select(Gender).where(Gender.name == name)
        return self.session.scalar(statement)
        
        
    def create(self,*,name:str) -> Gender :
        
        name = name.lower()
        
        existing_gender = self.get_by_name(name)
        
        if existing_gender is not None :
            raise ValueError("gender already exists")
            
        gender = Gender(name=name)
        
        self.session.add(gender)
        self.session.flush() 
        
        return gender 
    
    def delete(self,gender:Gender) -> None:
            
            self.session.delete(gender)
            self.session.flush()
    