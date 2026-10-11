
from settings import Model 
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import ForeignKey , String
from models.shared import TimeStamp
from typing import TYPE_CHECKING 

if TYPE_CHECKING :

        from models.utils import  AccessLevel
    

class Door(Model, TimeStamp) : 

    
    __tablename__="doors"
    
    id : Mapped[int] = mapped_column(primary_key=True , unique=True , nullable=False)
    name : Mapped[str] = mapped_column(String(32))
    location : Mapped[str] = mapped_column(String(256))
    access_id : Mapped[int] = mapped_column(ForeignKey("access_levels.id"))
    

    
    access : Mapped["AccessLevel"] = relationship(
        "AccessLevel"
        ,back_populates="doors")
    