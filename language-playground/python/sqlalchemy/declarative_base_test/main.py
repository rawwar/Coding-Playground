from models.base import Base
from models.user import User
from models.post import Post

from sqlalchemy import create_engine

engine = create_engine("sqlite:///user.db", echo=True)

Base.metadata.create_all(engine)