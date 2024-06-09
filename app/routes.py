from flask import Blueprint, request, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/notify', methods=['POST'])
def send_notification():
    data = request.get_json()
    # Here you would integrate with a notification service
    return jsonify({'message': 'Notification sent successfully', 'user_id': data['user_id']})
