import axiosInstance from './AxiosInstance';

const setAuthToken = (token) => {
    if (token) {
        axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    } else {
        delete axiosInstance.defaults.headers.common['Authorization'];
    }
};

function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}



const fetchData = (APICall) => {
  return axiosInstance.get(APICall)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching data:', error);
      throw error; // Rethrow the error for handling in the calling code
    });
};

async function postData(url, data) {
  try {
    const csrftoken = getCookie('csrftoken'); // Function to get CSRF token from cookie
    const response = await axiosInstance.post(url, data, {
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken // Include CSRF token in the request headers
      },
    });

    return response.data;
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
    throw error;
  }
}

const getData = async (url) => {
    try {
        const response = await axiosInstance.get(url);
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error; // Rethrow the error for handling in the calling code
    }
};



const updateData = async (tableData) => {
  let response;
  console.log(tableData)
  try {
    const response = await axiosInstance.post('/api/update-db/', tableData);
    console.log(response.data); // Log the response from the server
    return response.data;
    // Handle success if needed
  } catch (error) {
    console.error('Error updating data:', error);
    if (response) {
      console.log('Response from server:', response);
      return response.data;
      // Handle error with access to jsonResponse
    }    
    // Handle error
  }
};

const searchData = (query) => {
  console.log(query);
  return axiosInstance.get(query)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching data:', error);
      throw error; // Rethrow the error for handling in the calling code
    });
};



export default {fetchData, updateData, searchData, postData, getData, setAuthToken} ;