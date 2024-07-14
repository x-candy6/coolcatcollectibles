import { Navigate, Link } from "react-router-dom";
import React, { useContext, useState } from 'react';
import {AuthContext} from './AuthContext'
import Card from '../global/Card';
import API from '../api/API';

function Register() {
	const { setUser } = useContext(AuthContext);
	const [success, setSuccess] = useState(false);
	const [formData, setFormData] = useState({
		username: '',
		email:'',
		password: '',
		first_name: '',
		last_name: '',
		confirm_password: ''
	});

	const handleChange = e => {
	  const { name, value } = e.target;
	  setFormData(prevState => ({
	    ...prevState,
	    [name]: value
	  }));
	};

	const handleSubmit = async e => {
	  e.preventDefault();

	  try {
	    const response = await API.postData('/user/api/register/', formData);
	    const user = response; // Assuming the response contains user data
	    setUser(user.username); // Update user state after successful login
		console.log("Success")
		setSuccess(true)
	  } catch (error) {
	    console.error('Registration failed:', error);
	  }
	};

	if (success) {
	  return <Navigate to="/" replace />;
	}

    return ( 
		<>
        <Card>
        		<form onSubmit={handleSubmit} class="space-y-6" action="#" >
        			<h3 class="text-xl font-medium text-gray-900 dark:text-white">Register</h3>
        			<div>
        				<label for="email" class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300">Your email</label>
        				<input type="email" value={formData.email} onChange={handleChange} name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="name@company.com" required=""/>
                    </div>
        			<div>
        				<label for="username" class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300">Username</label>
        				<input type="username" name="username" value={formData.username} onChange={handleChange}  id="username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required=""/>
                    </div>
        			<div>
        				<label for="password" class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300">Your password</label>
        				<input type="password" name="password" id="password" value={formData.password} onChange={handleChange}  placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required=""/>
                    </div>


        			<div>
        				<label for="first_name" class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300">First Name</label>
        				<input type="name" name="first_name" value={formData.first_name} onChange={handleChange}  id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required=""/>
                    </div>

        			<div>
        				<label for="last_name" class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300">Last Name</label>
        				<input type="name" name="last_name" value={formData.last_name} onChange={handleChange}  id="last_name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required=""/>
                    </div>

        			<button type="submit" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Register</button>
        		</form>
        </Card>
		</>
     );
}

export default Register;