import React, { useState } from 'react';

function IndexBanner({slides}) {

    const [currentSlide, setCurrentSlide] = useState(0);

    const nextSlide = () => {
        setCurrentSlide((prevSlide) => (prevSlide + 1) % slides.length);
    };

    const prevSlide = () => {
        setCurrentSlide((prevSlide) => (prevSlide - 1 + slides.length) % slides.length);
    };

    const goToSlide = (index) => {
        setCurrentSlide(index);
    };

    return (
        <div className="w-full relative">
            <div className="relative w-full h-96 overflow-hidden">
                {slides.map((slide, index) => (
                    <a key={index} href={slide.href} className="block w-full h-full">
                        <img
                            src={slide.src}
                            alt={`Slide ${index + 1}`}
                            className={`absolute top-0 left-0 w-full h-full transform transition-transform duration-500 ${index === currentSlide ? 'translate-x-0 opacity-100' : 'translate-x-full opacity-0'}`}
                        />
                    </a>
                ))}
            </div>
            <button
                className="absolute top-1/2 left-4 transform -translate-y-1/2 bg-gray-800/50 text-white rounded-full p-2 hover:bg-gray-800 focus:outline-none"
                onClick={prevSlide}
            >
                Prev
            </button>
            <button
                className="absolute top-1/2 right-4 transform -translate-y-1/2 bg-gray-800/50 text-white rounded-full p-2 hover:bg-gray-800 focus:outline-none"
                onClick={nextSlide}
            >
                Next
            </button>
            <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
                {slides.map((_, index) => (
                    <button
                        key={index}
                        className={`w-3 h-3 rounded-full ${index === currentSlide ? 'bg-white' : 'bg-gray-400'}`}
                        onClick={() => goToSlide(index)}
                        aria-label={`Slide ${index + 1}`}
                    />
                ))}
            </div>
        </div>
    );
}

export default IndexBanner;
