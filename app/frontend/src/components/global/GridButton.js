function GridButton({children}) {
    return ( 
        <div className="bg-white rounded-xl shadow-md overflow-hidden">
            <div className="font-normal text-gray-700 dark:text-gray-400">
                {children}
            </div>
        </div>

     );
}

export default GridButton;