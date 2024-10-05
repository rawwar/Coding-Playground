from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(60), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    
    posts = relationship("Post", back_populates="author")
    
    def __repr__(self) -> str:
        return f"<User(username='{self.username}', email='{self.email}')>"
    