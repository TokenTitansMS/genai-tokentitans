from models.loan import Loan

class LoanRepository:
    @staticmethod
    def get_all_loans():
        return [loan.to_dict() for loan in Loan.query.all()]