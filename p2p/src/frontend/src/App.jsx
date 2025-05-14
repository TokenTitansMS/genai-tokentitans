import React, { useState } from 'react';
import RegisterForm from './components/Auth/RegisterForm';
import LoginForm from './components/Auth/LoginForm';

const App = () => {
  const [isLogin, setIsLogin] = useState(true);

  return (
    <div>
      <button onClick={() => setIsLogin(!isLogin)}>
        Switch to {isLogin ? 'Register' : 'Login'}
      </button>
      {isLogin ? <LoginForm /> : <RegisterForm />}
    </div>
  );
};

export default App;