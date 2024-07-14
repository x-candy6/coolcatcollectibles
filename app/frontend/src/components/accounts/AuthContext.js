import React, { useEffect, createContext, useState } from 'react';
import API from '../api/API';


export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // useEffect(() => {
  //     const token = localStorage.getItem('token');
  //     if (token) {
  //         // Fetch user data based on token or validate token
  //         fetchUserData(token);
  //     }
  // }, []);

  // const fetchUserData = async (token) => {
  //     try {
  //         // const response = await API.getData(`/user/api/user/${token}`);
  //         const response = await API.getData(`/user/api/user/${token}`);
  //         console.log(response)
  //         setAuthenticated(true);
  //         setUser(response);  // Set user state with user data from response
  //     } catch (error) {
  //         console.error('Error fetching user data:', error);
  //         setAuthenticated(false);
  //     }
  // };



  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
};
