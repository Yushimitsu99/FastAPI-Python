from turtle import title
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, true
from sqlalchemy.orm import relationship
from sqlalchemy.orm.interfaces import StrategizedProperty
from sqlalchemy.sql.elements import CollationClause
from sql_app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    ressources = relationship("Ressource", back_populates="owner")
    
class Ressource(Base):
    __tablename__ = "ressources"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    URL = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    owner = relationship("User", back_populates="ressources")