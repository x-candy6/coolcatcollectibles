import { useState } from "react";
import ReactSlider from "react-slider";

function FilterSidebar({ applyFilters }) {
    const [priceRange, setPriceRange] = useState((0, 100)); // Initial range from 0 to 100
    const [publisher, setPublisher] = useState('');
    const [era, setEra] = useState('');
    const [years, setYears] = useState('');
    const [character, setCharacter] = useState('');

    const handleApplyFilters = () => {
        const filters = {
            priceRange,
            publisher,
            era,
            years,
            character,
        };
        applyFilters(filters);
    };

    return (
        <div className="border-r-4 border-r-slate-400 filter-sidebar p-4">
            <h1 className="text-xl font-semibold mb-4">Filter Results</h1>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-1">Price Range</label>
                <ReactSlider
                    className="horizontal-slider"
                    thumbClassName="slider-point"
                    trackClassName="slider-track"
                    defaultValue={priceRange}
                    ariaLabelledby={['min-price', 'max-price']}
                    ariaValuetext={state => `Thumb value ${state.valueNow}`}
                    renderThumb={(props, state) => <div {...props}>{state.valueNow}</div>}
                    onChange={(value) => setPriceRange(value)}
                    pearling
                />
                <div className="flex justify-between text-sm text-gray-600">
                    <span>{priceRange[0]}</span>
                    <span>{priceRange[1]}</span>
                </div>
            </div>
            <input
                type="text"
                placeholder="Publisher"
                value={publisher}
                onChange={(e) => setPublisher(e.target.value)}
                className="input"
            />
            <input
                type="text"
                placeholder="Era"
                value={era}
                onChange={(e) => setEra(e.target.value)}
                className="input"
            />
            <input
                type="text"
                placeholder="Years"
                value={years}
                onChange={(e) => setYears(e.target.value)}
                className="input"
            />
            <input
                type="text"
                placeholder="Character"
                value={character}
                onChange={(e) => setCharacter(e.target.value)}
                className="input"
            />
            <button onClick={handleApplyFilters} className="bg-blue-500 text-white px-4 py-2 rounded-md mt-4 hover:bg-blue-600 focus:outline-none">
                Apply Filters
            </button>
        </div>
    );
}

export default FilterSidebar;