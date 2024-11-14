from flask import Blueprint

email_bp = Blueprint('email', __name__)

#func to get email
@email_bp.route('/email', methods=['GET'])
def get_email():
    return {'email': 'your_email@example.com'}