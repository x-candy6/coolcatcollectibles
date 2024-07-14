import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Replace with your Django server URL
  timeout: 8000, // Example timeout

});


export default axiosInstance ;