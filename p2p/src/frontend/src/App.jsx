import React, { useState } from 'react';
import RegisterForm from './components/Auth/RegisterForm';
import LoginForm from './components/Auth/LoginForm';
import TransactionForm from './components/Transaction/TransactionForm';
import Dashboard from './components/Dashboard/Dashboard';

const App = () => {
  const [view, setView] = useState('login'); // 'login', 'register', 'transaction', or 'dashboard'

  return (
    <div>
      <button onClick={() => setView(view === 'login' ? 'register' : 'login')}>
        Switch to {view === 'login' ? 'Register' : 'Login'}
      </button>
      {isLogin ? <LoginForm /> : <RegisterForm />}

      <LoanMarketplace />+
      <button onClick={() => setView('transaction')}>
        Go to Transaction Form
      </button>
      <button onClick={() => setView('dashboard')}>
        Go to Dashboard
      </button>

      {view === 'login' && <LoginForm />}
      {view === 'register' && <RegisterForm />}
      {view === 'transaction' && <TransactionForm />}
      {view === 'dashboard' && <Dashboard />}
      {isLogin ? <LoginForm onLoginSuccess={handleLoginSuccess} /> : <RegisterForm />}
    </div>
  );
  
};

export default App;