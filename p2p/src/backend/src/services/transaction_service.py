from repositories.transaction_repository import TransactionRepository
from models.transaction import Transaction

class TransactionService:
    @staticmethod
    def log_transaction(loan_id, lender_id, borrower_id, amount, transaction_type):
        transaction = Transaction(
            loan_id=loan_id,
            lender_id=lender_id,
            borrower_id=borrower_id,
            amount=amount,
            transaction_type=transaction_type
        )
        TransactionRepository.save(transaction)
        return {'message': 'Transaction logged successfully'}, 201