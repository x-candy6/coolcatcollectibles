import Card from "../global/Card";
import { useState, useEffect } from "react";
import API from "../api/API";

import Table from "../global/Tables/Table";
import TableOptions from "../global/Tables/TableOptions";
import Cell from "../global/Tables/Cell";
import SearchBar from "../global/Tables/SearchBar"


function GeneralInventory() {
    const dictionaries = [
        {"apple": "This is an apple", "ID": 1, "fruit": true},
        {"apple": "This is a pear", "ID": 2, "fruit": true}
    ];

    // Extract unique keys from dictionaries
    const allKeys = [...new Set(dictionaries.flatMap(Object.keys))];
    return ( 
        <>
            <Card>
                <SearchBar />
                <div>
                    <h1>Inventory Table</h1>
                    <Table headers={allKeys}>
                        {dictionaries.map((dict, index) => (
                            <tr key={index}>
                                {allKeys.map(key => (
                                    <Cell key={key}>
                                        {dict[key] !== undefined ? dict[key].toString() : ''}
                                    </Cell>
                                ))}
                            </tr>
                        ))}
                    </Table>
                </div>

                <TableOptions />
            </Card>
        </>
     );
}

export default GeneralInventory;