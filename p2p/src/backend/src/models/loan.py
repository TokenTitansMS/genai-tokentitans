from extensions import db

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(80), nullable=False)
    lender = db.Column(db.String(80), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # e.g., pending, approved, repaid

    def to_dict(self):
        return {
            'id': self.id,
            'borrower': self.borrower,
            'lender': self.lender,
            'amount': self.amount,
            'status': self.status
        }