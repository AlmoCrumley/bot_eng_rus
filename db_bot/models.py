from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

db_url = "sqlite:///db_bot/database.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    english = Column(String)
    russian = Column(String)

class UserVocabulary(Base):
    __tablename__ = 'user_vocabularies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word_id = Column(Integer, ForeignKey('words.id'))


Base.metadata.create_all(engine)

