
import uuid 
from models.users import User 
from settings import Model 
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import  Uuid , ForeignKey 
from models.shared import TimeStamp
from typing import TYPE_CHECKING 

if TYPE_CHECKING :
    
    from models.doors import Door
    from models.utils import CardStatus , AccessLevel , CardQr 

class Card(Model , TimeStamp) :
    
    __tablename__ = "cards"
    
    id : Mapped[uuid.UUID] = mapped_column(Uuid , primary_key=True , unique=True , nullable=False , default=uuid.uuid4)
    
    access_id : Mapped[int] = mapped_column(ForeignKey("access_levels.id"))
    
    status_id : Mapped[int] = mapped_column(ForeignKey("card_status.id"))  
    
    door_id : Mapped[int] = mapped_column(ForeignKey("doors.id"))
    
    qr_id : Mapped[uuid.UUID] = mapped_column(ForeignKey("qr_codes.id"))  
    
    
    status : Mapped["CardStatus"] = relationship(
        "CardStatus",
        back_populates="card"
    )
    
    access : Mapped["AccessLevel"] = relationship(
        "AccessLevel",
        back_populates="card"
        
    )
    user : Mapped["User"] = relationship(
        "User",
        back_populates="card")
    
    qr_code : Mapped["CardQr"] = relationship(
        "CardQr",
        back_populates="card"
    )
    
    door : Mapped["Door"] = relationship(
        "Door",
        back_populates="card"
    )