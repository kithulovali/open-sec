import uuid 
from utils import CardStatus , TimeStamp , AccessLevel , CardQr ,  Model 
from users import User 
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import  Uuid , ForeignKey 
from doors import Door


class Card(Model , TimeStamp) :
    
    __tablename__ = "cards"
    
    id : Mapped[uuid.UUID] = mapped_column(Uuid , primary_key=True , unique=True , nullable=False , default=uuid.uuid4)
    
    access_id : Mapped[int] = mapped_column(ForeignKey("access_level.id"))
    
    status_id : Mapped[int] = mapped_column(ForeignKey("card_status.id"))  
    
    door_id : Mapped[int] = mapped_column(ForeignKey("doors.id"))
    
    qr_id : Mapped[uuid.UUID] = mapped_column(ForeignKey("qr_codes.id"))  
    
    
    status : Mapped["CardStatus"] = relationship(
        back_populates="card"
    )
    
    access : Mapped["AccessLevel"] = relationship(
        back_populates="card"
        
    )
    user : Mapped["User"] = relationship(
        back_populates="card")
    
    qr_code : Mapped["CardQr"] = relationship(
        back_populates="card"
    )
    
    door : Mapped["Door"] = relationship(
        back_populates="card"
    )