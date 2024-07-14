import TableContainer from './TableContainer'

function TableCard({children}) {
    return ( 
        <TableContainer>
            <div className="bg-white rounded-xl shadow-md overflow-auto TableCard" style={{ flexGrow: 1 }}>
                {children}
            </div>
        </TableContainer>

     );
}

export default TableCard;