import Card from "../global/Card";
import API from "../api/API";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Product() {
    const { itemID } = useParams();
    const [product, setProduct] = useState({});
    const [itemInfo, setItemInfo] = useState({
        title: "",
        href: "",
        price: 0,
        currency: "$",
        qty: 0,
        image: ""
    });
    const [itemTags, setItemTags] = useState({
        publisher: "",
        date: "",
        description: "",
        era: "Golden Era"
    });

    useEffect(() => {
        const getProduct = async () => {
            try {
                console.log("Retrieving Product...");
                const url = `/inventory/api/product/${itemID}/`;
                const response = await API.getData(url);
                
                if (response && response.product) {
                    const { product } = response; // Destructure product from response
                    
                    // Update product state
                    setProduct(product);

                    // Update itemInfo state
                    setItemInfo({
                        title: product.listing_title,
                        href: `/product/${product.item_id}`,
                        price: product.price,
                        currency: "$",
                        qty: product.qty,
                        image: product.picurl
                    });

                    // Update itemTags state
                    setItemTags({
                        publisher: product.publisher,
                        date: product.release_date,
                        description: product.description,
                        era: "Golden Era"
                    });

                    console.log("Product retrieved:", product);
                } else {
                    console.log("Error retrieving product");
                }
            } catch (error) {
                console.error("Error retrieving product:", error);
            }
        };

        getProduct();
    }, [itemID]);

    return (
        <Card>
            <div className="flex flex-col md:flex-row gap-4">
                {/* Product Image */}
                <div className="md:w-1/2">
                    <img src={itemInfo.image} alt={itemInfo.title} className="w-full rounded-lg shadow-md" />
                </div>
                {/* Product Details */}
                <div className="md:w-1/2">
                    <h2 className="text-2xl font-bold mb-4">{itemInfo.title}</h2>
                    <p className="text-gray-600 mb-4">{itemTags.description}</p>
                    <p className="text-gray-800 font-bold text-xl mb-4">${itemInfo.price}</p>
                    <button className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-lg shadow-md">
                        Add to Cart
                    </button>
                </div>
            </div>
        </Card>
    );
}

export default Product;
