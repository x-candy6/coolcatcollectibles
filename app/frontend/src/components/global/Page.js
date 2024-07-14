import { AuthContext } from "../accounts/AuthContext";
import { Navigate, Link } from "react-router-dom";
import { useContext } from "react";
import { useState, useEffect } from "react";
import API from "../api/API";

function Page({children}) {
    const {user, setUser} = useContext(AuthContext)
    const [authenticated, setAuthenticated] = useState(false)

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
            // Fetch user data based on token or validate token
            fetchUserData(token);
        }
    }, []);

    const fetchUserData = async (token) => {
        try {
            // const response = await API.getData(`/user/api/user/${token}`);
            const response = await API.getData(`/user/api/user/${token}`);
            console.log(response)
            setAuthenticated(true);
            setUser(response);  // Set user state with user data from response
        } catch (error) {
            console.error('Error fetching user data:', error);
            setAuthenticated(false);
        }
    };


    return ( 
        <div class="Page">
            {children}
        </div>


     );
}

export default Page;