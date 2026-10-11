from sqlalchemy import select
from models.utils import UserStatus
from sqlalchemy.orm import Session 

class UserRoleRepository :
    
    def __init__(self ,session:Session):
        self.session = session 
        
    def get_status(self ,name :str) -> UserStatus | None :
        
        statement = select(UserStatus).where(UserStatus.name == name) 
        return self.session.scalar(statement)
    
    def create(self ,*, name :str , description:str) -> UserStatus :
        status = UserStatus(name=name , description=description) 
        self.session.add(status)
        self.session.flush()
        return status
    
    def update(self ,*,status : UserStatus, name :str | None ,
               description :str | None) -> UserStatus:
        
        if name is not None :
            status.name = name 
        if description is not None :
            status.description = description
            
        self.session.flush()
        return status
    
    def delete(self , status : UserStatus):
        self.session.delete(status)
        self.session.flush()
        