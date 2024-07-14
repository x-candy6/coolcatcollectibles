function AdvertBanner({children}) {
    return ( 
            <div class="bg-gray-100 p-4">
                <img src={children} alt="Banner" class="w-full max-w-full h-auto" />
            </div>
     );
}

export default AdvertBanner;