import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', 
  timeout: 8000, 

});

const setHeaders = (customHeaders) => {
  axiosInstance.defaults.headers = {
    ...axiosInstance.defaults.headers,
    ...customHeaders,
  };
};

export {axiosInstance, setHeaders} ;