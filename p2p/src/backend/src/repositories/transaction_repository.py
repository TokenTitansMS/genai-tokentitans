from models.transaction import Transaction
from extensions import db

class TransactionRepository:
    @staticmethod
    def save(transaction):
        db.session.add(transaction)
        db.session.commit()

    @staticmethod
    def get_by_loan_id(loan_id):
        return Transaction.query.filter_by(loan_id=loan_id).all()