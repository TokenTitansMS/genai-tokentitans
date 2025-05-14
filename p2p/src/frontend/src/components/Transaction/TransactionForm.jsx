import React, { useState } from 'react';
import { logTransaction } from '../../services/transactionService';

const TransactionForm = () => {
    const [loanId, setLoanId] = useState('');
    const [lenderId, setLenderId] = useState('');
    const [borrowerId, setBorrowerId] = useState('');
    const [amount, setAmount] = useState('');
    const [transactionType, setTransactionType] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await logTransaction({ loan_id: loanId, lender_id: lenderId, borrower_id: borrowerId, amount, transaction_type: transactionType });
            setMessage(response.message);
        } catch (error) {
            setMessage('Error logging transaction');
        }
    };

    return (
        <div>
            <h2>Log Transaction</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Loan ID:</label>
                    <input type="text" value={loanId} onChange={(e) => setLoanId(e.target.value)} required />
                </div>
                <div>
                    <label>Lender ID:</label>
                    <input type="text" value={lenderId} onChange={(e) => setLenderId(e.target.value)} required />
                </div>
                <div>
                    <label>Borrower ID:</label>
                    <input type="text" value={borrowerId} onChange={(e) => setBorrowerId(e.target.value)} required />
                </div>
                <div>
                    <label>Amount:</label>
                    <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} required />
                </div>
                <div>
                    <label>Transaction Type:</label>
                    <select value={transactionType} onChange={(e) => setTransactionType(e.target.value)} required>
                        <option value="">Select</option>
                        <option value="lending">Lending</option>
                        <option value="repayment">Repayment</option>
                    </select>
                </div>
                <button type="submit">Log Transaction</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default TransactionForm;