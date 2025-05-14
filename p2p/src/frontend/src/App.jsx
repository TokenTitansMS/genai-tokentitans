import React, { useState } from 'react';
import RegisterForm from './components/Auth/RegisterForm';
import LoginForm from './components/Auth/LoginForm';
import TransactionForm from './components/Transaction/TransactionForm';

const App = () => {
  const [view, setView] = useState('login'); // 'login', 'register', or 'transaction'

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
    </div>
  );
};

export default App;