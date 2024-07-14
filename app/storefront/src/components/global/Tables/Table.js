import Cell from "./Cell";

function Table({headers, children}) {
    return ( 
        <table className="table-auto " border="1">
            <thead>
                <tr>
                    {headers.map(header => (
                        <th key={header}>{header}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {children}
            </tbody>
        </table>
     );
}

export default Table;