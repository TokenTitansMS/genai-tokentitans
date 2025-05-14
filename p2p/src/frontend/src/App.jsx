import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import RegisterForm from './components/Auth/RegisterForm';
import LoginForm from './components/Auth/LoginForm';
import Dashboard from './components/Dashboard/Dashboard';

const App = () => {
  const [isLogin, setIsLogin] = useState(true);

  const navigate = useNavigate();

  const handleLoginSuccess = () => {
    navigate('/dashboard');
  };

  return (
    <div>
      <button onClick={() => setIsLogin(!isLogin)}>
        Switch to {isLogin ? 'Register' : 'Login'}
      </button>
      {isLogin ? <LoginForm onLoginSuccess={handleLoginSuccess} /> : <RegisterForm />}
    </div>
  );
};

export default App;