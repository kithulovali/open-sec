from sqlalchemy import select
from models.utils import UserRole
from sqlalchemy.orm import Session 

class UserRoleRepository :
    
    def __init__(self ,session:Session):
        self.session = session 
        
    def get_role(self ,name :str) -> UserRole | None :
        
        statement = select(UserRole).where(UserRole.name == name) 
        return self.session.scalar(statement)
    
    def create(self , name :str , description:str) -> UserRole :
        role = UserRole(name=name , description=description) 
        self.session.add(role)
        self.session.flush()
        return role
    
    def update(self ,role : UserRole, *,name :str | None ,
               description :str | None) -> UserRole:
        
        if name is not None :
            role.name = name 
        if description is not None :
            role.description = description
            
        self.session.flush()
        return role
    
    def delete(self , role: UserRole):
        self.session.delete(role)
        self.session.flush()
        