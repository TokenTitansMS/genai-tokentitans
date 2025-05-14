# filepath: c:\Users\Administrator\Documents\genai-tokentitans\p2p\src\backend\src\services\dashboard_service.py
from repositories.loan_repository import LoanRepository

class DashboardService:
    @staticmethod
    def get_dashboard_data():
        loans = LoanRepository.get_all_loans()
        return {
            'loans': loans
        }