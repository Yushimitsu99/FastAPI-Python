from pydantic import BaseModel

class RessourceBase (BaseModel):
    title: str
    URL: str 
    
class RessourceCreate(RessourceBase):
    pass

class Ressource (RessourceBase):
    id: int
    owner_id: int
    
    class Config:
        from_attributes = True
        
class UserBase(BaseModel):
    username: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    is_active: bool
    ressources: list[Ressource] = []
    
    class Config:
        from_attributes = True