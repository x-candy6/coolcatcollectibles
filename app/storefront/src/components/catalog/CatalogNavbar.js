function CatalogNavbar() {
    return (
        <nav className="bg-gray-300 py-4">
            <div className="max-w-7xl mx-auto px-4 flex justify-between items-center">
                {/* Left side: Products */}
                <div className="flex items-center space-x-4">
                    <h1 className="text-black text-lg font-semibold">Products</h1>
                </div>

                {/* Middle space */}
                <div className="flex-grow"></div>

                {/* Right side: Search bar and button */}
                <div className="flex items-center space-x-4">
                    <input
                        type="text"
                        placeholder="Search"
                        className="py-2 px-4 rounded-md bg-gray-400 text-white focus:outline-none focus:bg-gray-600"
                    />
                    <button className="py-2 px-4 bg-blue-600 hover:bg-blue-700 text-white rounded-md focus:outline-none">
                        Search
                    </button>
                </div>
            </div>
        </nav>
    );
}

export default CatalogNavbar;
