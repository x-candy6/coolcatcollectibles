import { useState, useEffect } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';
import  { useContext } from 'react';
import API from '../api/API';

function Logout() {
  const [success, setSuccess] = useState(false);
  const { setUser } = useContext(AuthContext);

  const handleLogout = async () => {
    try {
      await API.postData('/user/api/logout/');
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      setUser(null);
      console.log("Logout successful");
      setSuccess(true);
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  useEffect(() => {
    handleLogout(); 
  }, []); // Empty dependency array ensures this effect runs only once

  if (success) {
    return <Navigate to="/" replace />;
  }

  return (
    <>
      <div>Logging out...</div>
    </>
  );
}

export default Logout;
