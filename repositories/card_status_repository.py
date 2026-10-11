from sqlalchemy import select
from models.utils import CardStatus 
from sqlalchemy.orm import Session 

class UserRoleRepository :
    
    def __init__(self ,session:Session):
        self.session = session 
        
    def get_status(self ,name :str) -> CardStatus | None :
        
        statement = select(CardStatus).where(CardStatus.name == name) 
        return self.session.scalar(statement)
    
    def create(self , name :str , description:str) -> CardStatus :
        status = CardStatus(name=name , description=description) 
        self.session.add(status)
        self.session.flush()
        return status
    
    def update(self ,status : CardStatus, *,name :str | None ,
               description :str | None) -> CardStatus:
        
        if name is not None :
            status.name = name 
        if description is not None :
            status.description = description
            
        self.session.flush()
        return status
            
    
    def delete(self , status : CardStatus):
        self.session.delete(status)
        self.session.flush()
        