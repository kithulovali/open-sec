
import uuid 
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import String , Uuid , Integer , ForeignKey
from models.shared import TimeStamp
from settings import Model 
from typing import TYPE_CHECKING , List


if TYPE_CHECKING :
    from models.utils import  UserRole , Gender , UserStatus 
    from models.cards import Card 
    

class User(Model, TimeStamp):
    
    __tablename__ = "users"
    
    private_id : Mapped[uuid.UUID] = mapped_column(Uuid , primary_key=True , unique=True ,default=uuid.uuid4)
    public_id : Mapped[uuid.UUID] = mapped_column(Uuid , unique=True ,default=uuid.uuid4)
    name : Mapped[str] = mapped_column(String(32),nullable=False)
    email : Mapped[str] = mapped_column(String(256),nullable=False , unique=True)
    contact : Mapped[List[int]] = mapped_column(Integer)
    
    gender_id : Mapped[str] = mapped_column(ForeignKey("genders.id"))
    role_id : Mapped[int] = mapped_column(ForeignKey("roles.id"))
    card_id : Mapped[uuid.UUID] = mapped_column(ForeignKey("cards.id"))
    status_id : Mapped[int] = mapped_column(ForeignKey("user_status.id"))
    
    
    role : Mapped["UserRole"] = relationship(
        "UserRole",
        back_populates="user"
    )
    
    gender : Mapped["Gender"] = relationship(
        "Gender",
        back_populates="user"
        
        )
    
    card : Mapped["Card"] = relationship(
        "Card",
        back_populates="owner"
    )
    
    status : Mapped["UserStatus"] = relationship(
        "UserStatus",
        back_populates="status"
    )
    
  
    
    