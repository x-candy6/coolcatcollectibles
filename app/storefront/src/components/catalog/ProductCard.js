import { useState, useEffect } from "react";
import Divider from "../global/Divider";
function ProductCard({product, user}) {

    useEffect(() => {
        if (product) {
            setItemInfo({
                "title": product.listing_title,
                "href": `/product/${product.item_id}`,
                "price": product.price,
                "currency": "$",
                "qty": product.qty,
                "image": product.picurl
            });
            setItemTags({
                "publisher": product.publisher,
                "date": product.release_date,
                "era": product.time_era
            });
        }
    }, [product]);
    console.log(product)
    const [itemInfo, setItemInfo] = useState({
        "title": product.listing_title,
        "href":`/product/${product.item_id}`,
        "price": product.price,
        "currency": "$",
        "qty": product.qty,
        "image": product.picurl
    })
    const [itemTags, setItemTags] = useState({
        "publisher": product.publisher,
        "date": product.release_date,
        "era": "Golden Era",
    })



    return ( 
        <div className="border-3 border-blue-800 rounded-lg  product-card">
            <a href={itemInfo.href}>
                <div className="hover:bg-slate-200 max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                    <a href="#" className="flex justify-center">
                        <img src={itemInfo.image} alt="" />
                    </a>
                    <div className="p-5">
                        <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{itemInfo.title}</h5>
                        {Object.keys(itemTags).map((key) => (
                            <p key={key} className="inline-block px-3 py-1 mr-2 mb-2 rounded-lg bg-slate-200 hover:bg-slate-300">
                                {`${itemTags[key]}`}
                            </p>
                        ))}
                        <hr className="m-2"/>

                        <div href="#" className="inline-flex items-center ">
                            <h6>&nbsp; Price: {itemInfo.currency}{itemInfo.price}</h6>
                            <h6>&nbsp; Available: {itemInfo.qty}&nbsp;&nbsp;</h6>
                            <a className="px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </a>
        </div>
     );
}

export default ProductCard;