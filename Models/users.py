import uuid 
from utils import TimeStamp , UserRole , Gender , UserStatus , Model
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import String , Uuid , Integer , ForeignKey
from typing import List
from cards import Card 

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
        back_populates="user"
    )
    
    gender : Mapped["Gender"] = relationship(
        back_populates="user"
        )
    
    card : Mapped["Card"] = relationship(
        back_populates="owner"
    )
    
    status : Mapped["UserStatus"] = relationship(
        back_populates="status"
    )
    
  
    
    