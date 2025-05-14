from extensions import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, nullable=False)
    lender_id = db.Column(db.Integer, nullable=False)
    borrower_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # 'lending' or 'repayment'
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())