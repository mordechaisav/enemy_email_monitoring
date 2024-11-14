from sqlalchemy import Column, Integer, String, DateTime, Float, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from postgress_db import Base


class ExplosiveEmail(Base):
    __tablename__ = 'explosive_emails'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String)
    created_at = Column(DateTime)
    location_latitude = Column(Float)
    location_longitude = Column(Float)
    location_city = Column(String)
    location_country = Column(String)
    device_browser = Column(String)
    device_os = Column(String)
    device_id = Column(String)
    explosive_sentences = Column(ARRAY(String))
    sentences = Column(ARRAY(String))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='explosive_emails')
    def to_dict(self):
        return {
            'id': self.id,
            'ip_address': self.ip_address,
            'created_at': self.created_at,
            'location': {
                'latitude': self.location_latitude,
                'longitude': self.location_longitude,
                'city': self.location_city,
                'country': self.location_country
            },
            'device_info': {
                'browser': self.device_browser,
                'os': self.device_os,
                'device_id': self.device_id
            },
            'sentences': self.sentences,
            'explosive_sentences': self.hostage_sentences
        }
