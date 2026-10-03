from sqlalchemy.orm import DeclarativeBase 
from users import User
from cards import Card 
from datetime import datetime 
from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import DateTime , func  , String , Text , Uuid
import uuid
from doors import Door

class Model(DeclarativeBase):
    pass 

class TimeStamp:
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) 
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) 
    
    
class UserRole(Model,TimeStamp):
    __tablename__ = "roles"
    
    id : Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    name : Mapped[str] = mapped_column(String(32),nullable=False, unique=True)
    description : Mapped[str] = mapped_column(Text)
    
    user : Mapped["User"] = relationship(
        back_populates="role"
    ) 
    

class Gender(Model , TimeStamp):
    __tablename__="genders"
    
    id:Mapped[int] = mapped_column(primary_key=True ,nullable=False)
    name : Mapped[str] = mapped_column(String(32), nullable=True, unique=True)
    
    user : Mapped["User"] = relationship(
        back_populates="gender"
    ) 

class CardStatus(Model , TimeStamp):
    
    __tablename__="card_status"
    
    id : Mapped[int] = mapped_column(primary_key=True , nullable=False , unique=True)
    name : Mapped[str] = mapped_column(String(32), nullable=False , unique=True)
    description : Mapped[str] = mapped_column(Text)
    
    card : Mapped["Card"] = relationship(
        back_populates="status"
    )
    

class UserStatus(Model , TimeStamp):
    
    __tablename__="user_status"
    
    id : Mapped[int] = mapped_column(primary_key=True , unique=True , nullable=False)
    name : Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text)
    
    user : Mapped["User"] = relationship(
        back_populates="status"
    )
    
class AccessLevel(Model , TimeStamp):
    __tablename__="access_levels"
    
    id : Mapped[int] = mapped_column(primary_key=True , unique=True ,nullable=True)
    name : Mapped[str] = mapped_column(String(32),nullable=True , unique=True)
    description : Mapped[str] = mapped_column(Text)
    
    card : Mapped["Card"] = relationship(
        back_populates="access"
        )
    
    door : Mapped["Door"] = relationship(
        back_populates="access"
    )
    
class CardQr(Model , TimeStamp):
    
    __tablename__="qr_codes"
    
    id : Mapped[uuid.UUID] = mapped_column(Uuid , primary_key=True , unique=True ,nullable=False)
    
    user : Mapped["User"]  = relationship(
        back_populates="qr_code"
        )
    
    card : Mapped["Card"] = relationship(
        back_populates="qr_code"
        )