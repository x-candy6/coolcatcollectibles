import GridButton from "./GridButton";

function Grid({children}) {
    return ( 
        <div className="grid grid-cols-3 gap-2">
            {children}
        </div>
    );
}

export default Grid;