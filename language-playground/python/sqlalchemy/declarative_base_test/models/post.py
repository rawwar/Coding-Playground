from .base import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    author = relationship("User", back_populates="posts")
    
    def __repr__(self):
        return f"<Post(title='{self.title}', author='{self.author}')>"