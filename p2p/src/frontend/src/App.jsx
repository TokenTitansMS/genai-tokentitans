import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import RegisterForm from './components/Auth/RegisterForm';
import LoginForm from './components/Auth/LoginForm';
import TransactionForm from './components/Transaction/TransactionForm';
import Dashboard from './components/Dashboard/Dashboard';

const App = () => {
  const [view, setView] = useState('login'); // 'login', 'register', or 'transaction'

  const navigate = useNavigate();

  const handleLoginSuccess = () => {
    navigate('/dashboard');
  };

  return (
    <div>
      <button onClick={() => setView(view === 'login' ? 'register' : 'login')}>
        Switch to {view === 'login' ? 'Register' : 'Login'}
      </button>
      <button onClick={() => setView('transaction')}>
        Go to Transaction Form
      </button>

      {view === 'login' && <LoginForm />}
      {view === 'register' && <RegisterForm />}
      {view === 'transaction' && <TransactionForm />}
      {isLogin ? <LoginForm onLoginSuccess={handleLoginSuccess} /> : <RegisterForm />}
    </div>
  );
};

export default App;