from sqlalchemy import select
from models.utils import AccessLevel
from sqlalchemy.orm import Session 

class UserRoleRepository :
    
    def __init__(self ,session:Session):
        self.session = session 
        
    def get_access_level(self ,name :str) -> AccessLevel | None :
        
        statement = select(AccessLevel).where(AccessLevel.name == name) 
        return self.session.scalar(statement)
    
    
    def create(self , name :str , description:str) -> AccessLevel :
        access = AccessLevel(name=name , description=description) 
        self.session.add(access)
        self.session.flush()
        return access
    
    def update(self ,access:AccessLevel, *,name :str | None ,
               description :str | None) -> AccessLevel:
        
        if name is not None :
            access.name = name 
        if description is not None :
            access.description = description
            
        self.session.flush()
        return access
            
    
    def delete(self , access : AccessLevel):
        self.session.delete(access)
        self.session.flush()
        