import ProductCard from "./ProductCard";
import { useContext } from "react";
import { AuthContext } from "../accounts/AuthContext";

function Listings({ products }) {
    const { user } = useContext(AuthContext);

    return (
        <div className="product-listings grid gap-3 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5">
            {products.map((product, index) => (
                <ProductCard key={index} product={product} user={user} />
            ))}
        </div>
    );
}

export default Listings;
