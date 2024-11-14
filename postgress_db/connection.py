from postgress_db import Base
from postgress_db.config import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)
def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)