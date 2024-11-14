from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from postgress_db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    hostage_emails = relationship("HostageEmail",back_populates='user')
    explosive_emails = relationship("ExplosiveEmail",back_populates='user')
