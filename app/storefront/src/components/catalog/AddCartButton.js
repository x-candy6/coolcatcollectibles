import API from "../api/API"
import { useState } from "react";

function AddCartButton( {itemInfo} ) {
    const [cartItem, setCartItem] = useState({
        "sessionID": localStorage.getItem('session-id'),
        "itemID":itemInfo.item_id,
        "qty": 1, // TODO Change this to be dynamic later
    })
    const [success, setSuccess] = useState(false); // TODO will be used later to turn the T to a checkmark, and to popup a modal on error

	const handleClick = async e => {
        e.preventDefault()
        console.log(localStorage.getItem('session-id')); 
        console.log(itemInfo.item_id); 

	    try {
	        const response = await API.postData('/user/api/cart/add/',  cartItem);
		    console.log(response)

	        console.log("Successfully added to cart");
	        setSuccess(true);
	    } catch (error) {
	        console.error('Add to Cart failed:', error);
	    }
    };

    return ( 
        <button 
            className="px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            onClick={handleClick}
        >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" className="w-6 h-6">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
        </button>

     );
}

export default AddCartButton;