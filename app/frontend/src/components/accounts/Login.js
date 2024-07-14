import { Navigate, Link } from "react-router-dom";
import  { useContext, useState } from 'react';
import Card2 from '../global/Card2';
import API from '../api/API'
import { AuthContext } from "./AuthContext";

function Login() {
	const { user, setUser } = useContext(AuthContext);

	const [formData, setFormData] = useState({
		username:'',
		password:''
	});

	const [success, setSuccess] = useState(false);

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
	    const response = await API.postData('/user/api/login/', formData);
	    setUser(response); // Update user state after successful login
		console.log(response)

		localStorage.setItem('token', response.token);
		localStorage.setItem('username', response.username);
		localStorage.setItem('userid', response.userid);

		API.setAuthToken(response.token)

	    console.log("Success");
	    setSuccess(true);
	  } catch (error) {
	    console.error('Login failed:', error);
	  }
	};

	if (success) {
	  return <Navigate to="/" replace />;
	}

    return ( 
		<>
        <Card2>
        		<form onSubmit={handleSubmit} class="space-y-6" action="#">
        			<h3 class="text-xl font-medium text-gray-900 dark:text-white">Sign in to our platform</h3>
        			<div>
        				<label for="username" class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300">Username</label>
        				<input type="username" onChange={handleChange} value={formData.username} name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="username" required=""/>
                    </div>
        				<div>
        					<label for="password" class="text-sm font-medium text-gray-900 block mb-2 dark:text-gray-300">Password</label>
        					<input type="password" onChange={handleChange} value={formData.password} name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required=""/>
                        </div>
        					<div class="flex items-start">
        						<div class="flex items-start">
        							<div class="flex items-center h-5">
        								<input id="remember" aria-describedby="remember" type="checkbox" class="bg-gray-50 border border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800" required=""/>
                                    </div>
        								<div class="text-sm ml-3">
        									<label for="remember" class="font-medium text-gray-900 dark:text-gray-300">Remember me</label>
        								</div>
        							</div>
        							<Link to="#" class="text-sm text-blue-700 hover:underline ml-auto dark:text-blue-500">Lost
        								Password?</Link>
        						</div>
        						<button type="submit" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Login to your account</button>
        						<div class="text-sm font-medium text-gray-500 dark:text-gray-300">
        							Not registered? <Link to="#" class="text-blue-700 hover:underline dark:text-blue-500">Create
        								account</Link>
        						</div>
        		</form>
        </Card2>
		</>
     );
}

export default Login;