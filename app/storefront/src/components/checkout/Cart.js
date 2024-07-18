import API from "../api/API";
import { redirect } from "react-router-dom";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Card from "../global/Card";

function Cart() {

// fetch the relevant cart
// fetch the items from the inventory table
// display information

    // Dummy data
    const [cartItems, setCartItems] = useState([
        {
            id: 1,
            title: "Product 1",
            price: 29.99,
            quantity: 1,
            image: "https://via.placeholder.com/150",
        },
        {
            id: 2,
            title: "Product 2",
            price: 39.99,
            quantity: 2,
            image: "https://via.placeholder.com/150",
        },
    ]);


    useEffect(() => {

        const retrieveCart = async () => {
            console.log("Retrieving cart...");
            let url = '/user/api/cart/get/';
            // TODO If authenticated retrieve const user
            try {
                const response = await API.getData(url)
                console.log("Cart retrieved:", response)
                setCartItems(response.cart_items)
            } catch (error){
                console.log("Cart not retrieved:", error)

            }


        }
        retrieveCart()


    }, [])

    // Function to calculate total cart amount
    const calculateTotal = () => {
        return cartItems.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2);
    };

    const PayWithStripeButton = async () => {
        // Fetch the Checkout session from your backend
        const formData = {
            line_items: cartItems
        }
        try{ 
            const response = await API.postData('/orders/api/payments/stripe_checkout/', formData);

        } catch (error) {
            console.log(error.response.data.checkout_session_url)

            if (error.response.status === 303){
                 window.location.href = error.response.data.checkout_session_url
            } else{
                console.log(error.response.status)
                console.log("PayWithStripeButton Error:", error)

            }
        }

    };


    return (
        <Card>
        <div className="mx-auto py-8">
            <h2 className="text-2xl font-bold mb-4">Shopping Cart</h2>

            {/* Cart items */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {cartItems.map((item) => (
                    <div key={item.id} className="flex bg-white rounded-lg shadow-md overflow-hidden">
                        <img src={item.image} alt={item.title} className="w-24 h-24 object-cover" />
                        <div className="p-4 flex flex-col justify-between flex-grow">
                            <div>
                                <h3 className="text-lg font-semibold">{item.title}</h3>
                                <p className="text-gray-600">${item.price.toFixed(2)}</p>
                            </div>
                            <div className="flex items-center justify-between mt-4">
                                <div className="flex items-center">
                                    <button className="bg-gray-200 hover:bg-gray-300 px-2 py-1 rounded-md" onClick={() => console.log("Decrease quantity")}>-</button>
                                    <span className="mx-2">{item.quantity}</span>
                                    <button className="bg-gray-200 hover:bg-gray-300 px-2 py-1 rounded-md" onClick={() => console.log("Increase quantity")}>+</button>
                                </div>
                                <p className="font-semibold">${(item.price * item.quantity).toFixed(2)}</p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {/* Cart summary */}
            <div className="mt-8 flex justify-between items-center">
                <p className="text-xl font-semibold">Total:</p>
                <p className="text-xl font-semibold">${calculateTotal()}</p>
            </div>

            {/* Stripe Checkout button */}
            <div className="border-solid border-2 border-indigo-600 mt-8 flex justify-end">
                <button 
                    className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md shadow-md"
                    onClick={PayWithStripeButton}
                >
                    Pay with Stripe
                </button>
            </div>
        </div>
        </Card>
    );
}

export default Cart;
