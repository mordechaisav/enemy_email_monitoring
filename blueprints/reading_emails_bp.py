from flask import Blueprint, request, jsonify
import json
from kafka import KafkaProducer
from blueprints.service import analyze_email, reorder_sentences
from postgress_db import HostageEmail, ExplosiveEmail
from postgress_db.connection import session_maker
from postgress_db.user_model import User

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
bp_email = Blueprint('email', __name__)


@bp_email.route('/api/email', methods=['POST'])
def get_email():
    data = request.get_json()
    producer.send('messages_all',value=data)
    print("send to message all")
    result = analyze_email(data)
    new_data = reorder_sentences(data)
    if result == "hostage":
        producer.send('topic_hostage', value=new_data)
    if result == "explos":
        producer.send('topic_explosive', value=new_data)

    return jsonify({'message': 'Email sent successfully'}), 200


@bp_email.route('/fraud', methods=['GET'])
def get_all_fraud_emails():
    data = request.get_json()
    email = data["email"]
    session = session_maker()
    result = session.query(User).filter_by(email=email).join(HostageEmail,ExplosiveEmail).all()
    session.close()
    if not result:
        return jsonify({"error": "No fraud emails found"}), 200



    messages = []
    for message in result:
        message["_id"] = str(message["_id"])
        messages.append(message)
    return jsonify({"messages": messages}), 200
