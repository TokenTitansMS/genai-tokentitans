# filepath: c:\Users\Administrator\Documents\genai-tokentitans\p2p\src\backend\src\controllers\dashboard_controller.py
from flask import Blueprint, jsonify
from services.dashboard_service import DashboardService

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    try:
        data = DashboardService.get_dashboard_data()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500