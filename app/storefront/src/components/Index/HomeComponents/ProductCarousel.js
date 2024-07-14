import React, { useState, useRef } from 'react';

function ProductCarousel( {bannerTitle}) {
    const carouselRef = useRef(null);

    function scrollCarousel(direction) {
        const carousel = carouselRef.current;
        const scrollAmount = carousel.offsetWidth;
        if (direction === 'left') {
            carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        } else {
            carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
    }

    return (
        <div className="bg-gray-100">
            <div className="mx-auto py-8">
                <h2 className="text-2xl font-bold mb-4">{bannerTitle}</h2>
                <div className="carousel-container relative">
                    <button 
                        className="carousel-button carousel-button-left absolute left-0 top-1/2 transform -translate-y-1/2 bg-black bg-opacity-50 text-white p-2 rounded-full"
                        onClick={() => scrollCarousel('left')}
                    >
                        &lt;
                    </button>
                    <div 
                        className="carousel flex items-center overflow-x-auto scroll-snap-x scroll-snap-mandatory"
                        ref={carouselRef}
                    >
                        {/* Product 1 */}
                        <div className="carousel-item bg-white p-4 rounded-lg shadow-md flex-none mr-4 scroll-snap-align-center">
                            <img src="https://via.placeholder.com/150" alt="Product 1" className="max-h-48 w-auto"/>
                            <h3 className="mt-2 font-semibold">Product 1</h3>
                            <p className="mt-1 text-gray-600">$29.99</p>
                        </div>
                        {/* Product 2 */}
                        <div className="carousel-item bg-white p-4 rounded-lg shadow-md flex-none mr-4 scroll-snap-align-center">
                            <img src="https://via.placeholder.com/150" alt="Product 2" className="max-h-48 w-auto"/>
                            <h3 className="mt-2 font-semibold">Product 2</h3>
                            <p className="mt-1 text-gray-600">$39.99</p>
                        </div>
                        {/* Product 3 */}
                        <div className="carousel-item bg-white p-4 rounded-lg shadow-md flex-none mr-4 scroll-snap-align-center">
                            <img src="https://via.placeholder.com/150" alt="Product 3" className="max-h-48 w-auto"/>
                            <h3 className="mt-2 font-semibold">Product 3</h3>
                            <p className="mt-1 text-gray-600">$49.99</p>
                        </div>
                        {/* Product 4 */}
                        <div className="carousel-item bg-white p-4 rounded-lg shadow-md flex-none mr-4 scroll-snap-align-center">
                            <img src="https://via.placeholder.com/150" alt="Product 4" className="max-h-48 w-auto"/>
                            <h3 className="mt-2 font-semibold">Product 4</h3>
                            <p className="mt-1 text-gray-600">$59.99</p>
                        </div>

                        {/* Product 4 */}
                        <div className="carousel-item bg-white p-4 rounded-lg shadow-md flex-none mr-4 scroll-snap-align-center">
                            <img src="https://via.placeholder.com/150" alt="Product 4" className="max-h-48 w-auto"/>
                            <h3 className="mt-2 font-semibold">Product 4</h3>
                            <p className="mt-1 text-gray-600">$59.99</p>
                        </div>
                    </div>
                    <button 
                        className="carousel-button carousel-button-right absolute right-0 top-1/2 transform -translate-y-1/2 bg-black bg-opacity-50 text-white p-2 rounded-full"
                        onClick={() => scrollCarousel('right')}
                    >
                        &gt;
                    </button>
                </div>
            </div>
        </div>
    );
}

export default ProductCarousel;
