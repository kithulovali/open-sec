from datetime import datetime 
from sqlalchemy.orm import Mapped , mapped_column 
from sqlalchemy import DateTime , func 

class TimeStamp:
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) 
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) 