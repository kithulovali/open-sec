
from settings import Model 
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import ForeignKey
from models.shared import TimeStamp
from typing import TYPE_CHECKING 

if TYPE_CHECKING :
        from models.cards import Card
        from models.utils import  AccessLevel
    

class Door(Model, TimeStamp) : 

    
    __tablename__="doors"
    
    id : Mapped[int] = mapped_column(primary_key=True , unique=True , nullable=False)
    
    access_id : Mapped[int] = mapped_column(ForeignKey("doors.id"))
    
    card : Mapped["Card"] = relationship(
        "Door"
        ,back_populates="door")
    
    access : Mapped["AccessLevel"] = relationship(
        "AccessLevel"
        ,back_populates="door")
    