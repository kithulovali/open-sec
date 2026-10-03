

from cards import Card
from utils import Model , TimeStamp , AccessLevel
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import ForeignKey

class Door(Model, TimeStamp) : 
    
    __tablename__="doors"
    
    id : Mapped[int] = mapped_column(primary_key=True , unique=True , nullable=False)
    
    access_id : Mapped[int] = mapped_column(ForeignKey("doors.id"))
    
    card : Mapped["Card"] = relationship(back_populates="door")
    
    access : Mapped["AccessLevel"] = relationship(back_populates="door")
    