import { useContext, useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";
import CatalogNavbar from "./CatalogNavbar";
import CatalogCard from "./CatalogCard";
import Divider from "../global/Divider";
import FilterSidebar from "./FilterSidebar";
import Listings from "./Listings";
import { AuthContext } from "../accounts/AuthContext";
import API from "../api/API";

function Catalog() {
    const { user } = useContext(AuthContext);
    const [products, setProducts] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [filters, setFilters] = useState({});

    const { searchCategory } = useParams();
    const location = useLocation();

    useEffect(() => {
        const getCatalog = async () => {
            console.log("Retrieving catalog...");
            let url = '/inventory/api/catalog/';

            // Build query parameters based on filters state
            const params = { page: currentPage, ...filters };
            const queryParams = new URLSearchParams(params).toString();
            url += `?${queryParams}`;

            try {
                const response = await API.getData(url);
                console.log("Catalog Successfully Retrieved:", response);
                if (response && response.products) {
                    setProducts(response.products);
                    setTotalPages(response.total_pages);
                    console.log("Successfully set client-side product data");
                }
            } catch (error) {
                console.error("Catalog Fetch Failed:", error);
            }
        };

        getCatalog();
    }, [searchCategory, location.pathname, currentPage, filters]);

    const handleApplyFilters = (newFilters) => {
        setCurrentPage(1); // Reset to first page when filters change
        setFilters(newFilters);
    };

    const nextPage = () => {
        if (currentPage < totalPages) {
            setCurrentPage(currentPage + 1);
        }
    };

    const prevPage = () => {
        if (currentPage > 1) {
            setCurrentPage(currentPage - 1);
        }
    };

    return (
        <CatalogCard>
            <div className="catalog">
                {/* Add the search feature later - it is P3 */}
                {/* <CatalogNavbar /> */}
                <Divider />
                <div className="catalog-wrapper">
                    <FilterSidebar applyFilters={handleApplyFilters} />
                    <Listings products={products} />
                    <div className="pagination-wrapper">
                        <div className="pagination flex justify-center items-center">
                            <button onClick={prevPage} disabled={currentPage === 1} className="mr-2">
                                Previous
                            </button>
                            <span className="mx-4">
                                Page {currentPage} of {totalPages}
                            </span>
                            <button onClick={nextPage} disabled={currentPage === totalPages} className="ml-2">
                                Next
                            </button>
                        </div>
                    </div>


                </div>
            </div>
        </CatalogCard>
    );
}

export default Catalog;
