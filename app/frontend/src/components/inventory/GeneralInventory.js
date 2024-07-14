import TableCard from "../global/Tables/TableCard";
import { useState, useContext, useEffect } from "react";
import API from "../api/API";
import { AuthContext } from "../accounts/AuthContext";
import Table from "../global/Tables/Table";
import TableOptions from "../global/Tables/TableOptions";
import Cell from "../global/Tables/Cell";
import SearchBar from "../global/Tables/SearchBar";

function GeneralInventory() {
    const { user } = useContext(AuthContext);
    const [data, setData] = useState([]);  // holds inventory data
    const [headers, setHeaders] = useState([]);  // holds categories
    const [searchKey, setSearchKey] = useState(0); // Initialize search key state

    // Retrieves inventory on initial render
    useEffect(() => {
        const getInitialInventory = async () => {
            try {
                const response = await API.getData(`/inventory/api/general/${user.token}/`);
                console.log('Initial Inventory data:', response);

                if (response && response.headers && response.inventory) {
                    setHeaders(Object.values(response.headers));
                    setData(response.inventory);
                    console.log("Initial Fetch Complete");
                }
            } catch (error) {
                console.error('Initial Inventory retrieval failed:', error);
            }
        };
        getInitialInventory();

    }, [user.token]); // Added user.token to dependency array to avoid missing dependency warning

    const handleCellSave = async (rowIndex, key, newValue) => {
        const itemId = data[rowIndex].item_id;
        console.log(`Row: ${rowIndex}, Item ID: ${itemId}, Column: ${key}, New Value: ${newValue}`);
        const updatedItem = {
            'item_id': itemId,
            'column_name': key,
            'new_value': newValue
        }

        const response = await API.postData(`/inventory/api/updateItem/`, updatedItem);

        console.log(response);

        const newData = [...data];
        newData[rowIndex][key] = newValue;
        setData(newData);
    };

    const handleSearch = async (category, query) => {
        try {
            // Encode the query to ensure it is URL safe
            const res = await API.getData(`/inventory/api/search/${encodeURIComponent(category)}/${encodeURIComponent(query)}/`);
            console.log('Search data:', res);

            if (res && res.inventory) {
                console.log("Setting data to search results...");
                setData(res.inventory);
                setSearchKey(searchKey + 1);  // Update searchKey to force re-render if necessary
            }
        } catch (error) {
            console.error('Search failed:', error);
        }
    };

    return (
        <TableCard key={searchKey}>
            <SearchBar headers={headers} onSearch={handleSearch} />
            <div>
                <h1>Inventory Table</h1>
                <Table headers={headers}>
                    {data.map((dict, rowIndex) => (
                        <tr key={rowIndex}>
                            {headers.map((key) => (
                                <Cell
                                    key={`${rowIndex}-${key}`}
                                    initialValue={dict[key] !== undefined ? dict[key].toString() : ''}
                                    onSave={(newValue) => handleCellSave(rowIndex, key, newValue)}
                                />
                            ))}
                        </tr>
                    ))}
                </Table>
            </div>
            <TableOptions />
        </TableCard>
    );
}

export default GeneralInventory;
