"""#{
"email": "jeremy37@example.org",
"username": "jonesalejandra",
"ip_address": "215.67.111.124",
"created_at": "2024-10-15T05:29:13.450066",
"location": {
"latitude": 8.5478895,
"longitude": -135.24204,
"city": "Port Josephburgh",
"country": "PA"
},
"device_info": {
"browser": "Mozilla/5.0",
"os": "iOS",
"device_id": "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"
},
"sentences": [
"Public quickly spend hear sing.",
"Difference nothing environmental shake decide.",
"Natural southern what nice."
]
}"""
from sqlalchemy import Column, Integer, String, DateTime, Float, ARRAY

from postgress_db import Base


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    ip_address = Column(String)
    created_at = Column(DateTime)
    location_latitude = Column(Float)
    location_longitude = Column(Float)
    location_city = Column(String)
    location_country = Column(String)
    device_browser = Column(String)
    device_os = Column(String)
    device_id = Column(String)
    sentences = Column(ARRAY(String))
    def __repr__(self):
        return f'<Email(id={self.id}, email={self.email}, username={self.username})>'
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
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
            'sentences': self.sentences
        }


