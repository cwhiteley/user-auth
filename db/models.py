from sqlalchemy import ForeignKey, Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.init_db import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key= True, index=True)
    email = Column(String, unique=True, index=True)
    pw = Column(String)
    is_active = Column(Boolean, default=True)