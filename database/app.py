from sqlalchemy.orm import sessionmaker, Session

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

users = session.query(User).all()

print(users[0].name)
