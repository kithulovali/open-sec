
import uuid 
from models.users import User 
from settings import Model 
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import  Uuid , ForeignKey ,String
from models.shared import TimeStamp
from typing import TYPE_CHECKING 

if TYPE_CHECKING :
    
    from models.utils import CardStatus , AccessLevel 

class Card(Model , TimeStamp) :
    
    __tablename__ = "cards"
    
    id : Mapped[uuid.UUID] = mapped_column(Uuid , primary_key=True , unique=True , nullable=False , default=uuid.uuid4)
    
    card_name : Mapped[uuid.UUID] = mapped_column(Uuid, unique=True , nullable=False , default=uuid.uuid4)
        
    qr_code : Mapped[str] = mapped_column(String(256))
    
    user_id : Mapped[uuid.UUID] = mapped_column(ForeignKey("users.private_id"), nullable=False)
    
    access_id : Mapped[int] = mapped_column(ForeignKey("access_levels.id"),nullable=False)
    
    status_id : Mapped[int] = mapped_column(ForeignKey("card_status.id"),nullable=False)     
    
    
    
    status : Mapped["CardStatus"] = relationship(
        "CardStatus",
        back_populates="card"
    )
    
    access : Mapped["AccessLevel"] = relationship(
        "AccessLevel",
        back_populates="cards"
        
    )
    user : Mapped["User"] = relationship(
        "User",
        back_populates="cards")
    
