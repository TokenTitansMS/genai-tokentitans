from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
db = SQLAlchemy(app)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)

@app.route('/api/loans', methods=['GET'])
def get_loans():
    loans = Loan.query.all()
    return jsonify([{'id': loan.id, 'amount': loan.amount, 'description': loan.description} for loan in loans])

@app.route('/api/loans', methods=['POST'])
def create_loan():
    data = request.json
    new_loan = Loan(amount=data['amount'], description=data['description'])
    db.session.add(new_loan)
    db.session.commit()
    return jsonify({'id': new_loan.id, 'amount': new_loan.amount, 'description': new_loan.description}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)