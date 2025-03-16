// src/UserInfo.js
import React, { useEffect, useState } from 'react';

function UserInfo() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // You could call an endpoint that returns user info once authenticated.
    // For now, this is just a placeholder.
    fetch('http://localhost:8000/api/v1/user')  // Ensure your backend provides such an endpoint.
      .then((res) => res.json())
      .then((data) => setUser(data))
      .catch((err) => console.error(err));
  }, []);

  if (!user) return <div>Loading user info...</div>;

  return (
    <div>
      <h2>Welcome, {user.login || 'User'}!</h2>
      <pre>{JSON.stringify(user, null, 2)}</pre>
    </div>
  );
}

export default UserInfo;
