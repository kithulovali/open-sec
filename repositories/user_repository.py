from sqlalchemy import select 
from models.users import User
from sqlalchemy.orm import Session 
from typing import List

class DoorRepository :
    
    def __init__(self ,session : Session ):
        self.session = session
        
    def get_user(self ,email : str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.scalar(statement)
    
        
    def get_all_users(self ,*,offset :int = 0 
                      ,limit : int = 100) -> List[User] :
        statement = (select(User).order_by(User.email).offset(offset).limit(limit))
        return list(self.session.scalars(statement).all())
    
    
    def create(self ,*, name : str , email:str
               ,contact :str) -> User :
        
        existing_user = self.get_user(email)
        if existing_user is not None :
            raise ValueError("Door ALready Exists")
        
        user = User(name = name ,email=email , contact = contact)
        self.session.add(user)
        self.session.flush()
        return user 
    
    
    def update(self ,user : User , *,name :str | None , email : str | None 
               , contact : int | None) -> User :
        
        if name is not None :
            User.name = name 
        
        if email is not None :
            User.email = email
        
        if contact is not None :
            User.contact = contact 
     
        self.session.flush()
        return user
        
    
    def delete(self , user:User) -> None:
        self.session.delete(user)
        self.session.flush()