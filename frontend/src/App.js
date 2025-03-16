// src/App.js
import React from 'react';

function App() {
  // When the button is clicked, redirect to your backend OAuth endpoint.
  const handleLogin = () => {
    // Change the URL if your backend is hosted elsewhere.
    window.location.href = 'http://localhost:8000/api/v1/auth';
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Login Page</h1>
      <button onClick={handleLogin}>Login with GitHub</button>
    </div>
  );
}

export default App;
