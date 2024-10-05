from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.user import User
from models.post import Post

from faker import Faker
from random import randint

engine = create_engine("sqlite:///user.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

for _ in range(100):
    user = User(username=fake.unique.name(), email=fake.unique.email())
    session.add(user)

for user in session.query(User).all():
    for _ in range(randint(1,10)):
        post = Post(title=fake.sentence(), content=fake.text(), author=user)
        session.add(post)

session.commit()

session.close()