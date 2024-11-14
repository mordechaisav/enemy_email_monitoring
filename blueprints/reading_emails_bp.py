from flask import Blueprint, request
from kafka_files.produser.produser import get_message
email_bp = Blueprint('email', __name__)

#func to get email
@email_bp.route('/email', methods=['GET'])
def get_email():
    email = request.json.get('email')
    get_message(email)
    return {'email': 'send successfully'}