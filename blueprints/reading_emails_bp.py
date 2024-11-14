from flask import Blueprint, request, jsonify
import json
from kafka import KafkaProducer


from blueprints.service import check_email, change_senteness
from kafka_files.produser.mongoDB import collection
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
    result = check_email(data)
    new_data = change_senteness(data)
    if result == "hostage":
        producer.send('topic_hostage', value=new_data)
    if result == "explos":
        producer.send('topic_explosive', value=new_data)

    return jsonify({'message': 'Email sent successfully'}), 200

# @bp_email.route('/allemail', methods=['GET'])
# def get_all_messages_by_email():
#     data = request.get_json()
#     email = data['email']
#     if not email:
#         return jsonify({"error": "Email parameter is required"}), 400
#
#     result = collection.find({"email": email})
#     messages = []
#     for message in result:
#         message["_id"] = str(message["_id"])
#         messages.append(message)
#     return jsonify({"messages": messages}), 200
#find all fraud emails
@bp_email.route('/fraud', methods=['GET'])
def get_all_fraud_emails():
    data = request.get_json()
    email = data["email"]
    session = session_maker()
    result = session.query(User).filter_by(email=email).join(HostageEmail,ExplosiveEmail).all()
    session.close()
    if not result:
        return jsonify({"error": "No fraud emails found"}), 200
    #find the word הכי הרבה פעמים


    messages = []
    for message in result:
        message["_id"] = str(message["_id"])
        messages.append(message)
    return jsonify({"messages": messages}), 200
