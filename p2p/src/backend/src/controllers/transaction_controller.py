from flask import Blueprint, request, jsonify
from services.transaction_service import TransactionService

transaction_blueprint = Blueprint('transaction', __name__)

@transaction_blueprint.route('/log', methods=['POST'])
def log_transaction():
    data = request.json
    loan_id = data.get('loan_id')
    lender_id = data.get('lender_id')
    borrower_id = data.get('borrower_id')
    amount = data.get('amount')
    transaction_type = data.get('transaction_type')
    return TransactionService.log_transaction(loan_id, lender_id, borrower_id, amount, transaction_type)