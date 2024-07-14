import { useState, useEffect } from "react";
import Divider from "../global/Divider";
import AddCartButton from "./AddCartButton"
function ProductCard({product, user}) {

    useEffect(() => {
        if (product) {
            setItemInfo({
                "item_id": product.item_id,
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
        "item_id": product.item_id,
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
                <div className="hover:bg-slate-200 max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                    <a href={itemInfo.href} className="flex justify-center">
                        <img src={itemInfo.image} alt="" />
                    </a>
                    <div className="p-5">
                        <a href={itemInfo.href} ><h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{itemInfo.title}</h5></a>
                        {Object.keys(itemTags).map((key) => (
                            <p key={key} className="inline-block px-3 py-1 mr-2 mb-2 rounded-lg bg-slate-200 hover:bg-slate-300">
                                {`${itemTags[key]}`}
                            </p>
                        ))}
                        <hr className="m-2"/>

                        <div href="#" className="inline-flex items-center ">
                            <h6>&nbsp; Price: {itemInfo.currency}{itemInfo.price}</h6>
                            <h6>&nbsp; Available: {itemInfo.qty}&nbsp;&nbsp;</h6>
                            <AddCartButton itemInfo={itemInfo}/>
                        </div>
                    </div>
                </div>
        </div>
     );
}

export default ProductCard;