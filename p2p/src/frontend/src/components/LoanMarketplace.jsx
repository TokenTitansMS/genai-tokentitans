import React, { useState, useEffect } from 'react';

const LoanMarketplace: React.FC = () => {
  const [loans, setLoans] = useState([]);
  const [formData, setFormData] = useState({ amount: '', description: '' });

  useEffect(() => {
    // Fetch loans from the backend
    fetch('/api/loans')
      .then((response) => response.json())
      .then((data) => setLoans(data));
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetch('/api/loans', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((newLoan) => setLoans((prevLoans) => [...prevLoans, newLoan]));
  };

  return (
    <div>
      <h1>Loan Marketplace</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Loan Amount"
          value={formData.amount}
          onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
        />
        <textarea
          placeholder="Loan Description"
          value={formData.description}
          onChange={(e) =>
            setFormData({ ...formData, description: e.target.value })
          }
        />
        <button type="submit">Post Loan</button>
      </form>
      <h2>Available Loans</h2>
      <ul>
        {loans.map((loan: any) => (
          <li key={loan.id}>
            {loan.amount} - {loan.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LoanMarketplace;