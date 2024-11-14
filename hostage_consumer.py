import json
from kafka import KafkaConsumer

from postgress_db import HostageEmail
from postgress_db.connection import init_db, session_maker
from postgress_db.user_model import User

consumer = KafkaConsumer(
    'topic_hostage',
    bootstrap_servers='localhost:9092',
    group_id='group_hostage',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def save_email(data, user_id):
    email = HostageEmail(
        ip_address=data['ip_address'],
        created_at=data['created_at'],
        location_latitude=data['location']['latitude'],
        location_longitude=data['location']['longitude'],
        location_city=data['location']['city'],
        location_country=data['location']['country'],
        device_browser=data['device_info']['browser'],
        device_os=data['device_info']['os'],
        device_id=data['device_info']['device_id'],
        sentences=data['sentences'],
        user_id=user_id
    )
    session = session_maker()
    session.add(email)
    session.commit()
    session.refresh(email)

init_db()
for message in consumer:
    data = message.value
    user_email = data['email']
    username = data['username']
    session = session_maker()
    user = session.query(User).filter_by(email=user_email).first()

    if not user:
        user = User(username=username, email=user_email)
        session.add(user)
        session.commit()
        session.refresh(user)
    
    save_email(data, user.id)
    print('The email saved successfully')
    consumer.commit()
    session.close()