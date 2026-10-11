from sqlalchemy import select 
from models.doors import Door
from sqlalchemy.orm import Session 
from typing import List

class DoorRepository :
    
    def __init__(self ,session : Session ):
        self.session = session
        
    def get_door(self ,name : str) -> Door | None:
        statement = select(Door).where(Door.name == name)
        return self.session.scalar(statement)
    
        
    def get_all_doors(self ,*,offset :int = 0 
                      ,limit : int = 100) -> List[Door] :
        statement = (select(Door).order_by(Door.id).offset(offset).limit(limit))
        return list(self.session.scalars(statement).all())
    
    
    def create(self ,*, name : str 
               ,location :str) -> Door :
        
        existing_door = self.get_door(name)
        if existing_door is not None :
            raise ValueError("Door ALready Exists")
        
        door = Door(name = name , location = location)
        self.session.add(door)
        self.session.flush()
        return door 
    
    
    def update(self ,door : Door , *,name :str | None
               , location : str | None) -> Door :
        
        if name is not None :
            door.name = name 
        if location is not None :
            door.location = location 
        self.session.flush()
        return door
        
    
    def delete(self , door:Door) -> None:
        self.session.delete(door)
        self.session.flush()