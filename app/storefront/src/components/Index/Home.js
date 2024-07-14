import Card from "../global/Card"
import ProductCarousel from "./HomeComponents/ProductCarousel"
import ImageCarousel from "./HomeComponents/ImageCarousel"
import AdvertBanner from "./HomeComponents/AdvertBanner"
import TripleCard from "./HomeComponents/TripleCard"
import Divider from "../global/Divider"
import Page from "../global/Page"
function Home() {

    const main_carousel_slides = [
        {src:"https://images.pexels.com/photos/20787/pexels-photo.jpg?cs=srgb&dl=pexels-kmerriman-20787.jpg&fm=jpg", href:"/hello"},
        {src:"https://upload.wikimedia.org/wikipedia/commons/7/74/A-Cat.jpg", href:"/bye"}
    ]

    const sales_banner = {src:"https://3c5239fcccdc41677a03-1135555c8dfc8b32dc5b4bc9765d8ae5.ssl.cf1.rackcdn.com/22-12-28-BANS-sale-banner-1025x325-riot.jpg", href:"/"}

    return ( 
        <Page>
            <div className="home">
                {/* Sales Banner */}
                <div className="w-full Sale-Banner">
                    <a href={sales_banner.href}><img className="w-full" src={sales_banner.src}></img></a>

                </div>

                {/* Carousel Images */}
                <Divider />
                <div className="Carousel-Banner">
                    <ImageCarousel slides={main_carousel_slides} />

                </div>

                {/* Item Showcase */}
                <Divider />
                <div className="Product-Carousel">
                    <ProductCarousel bannerTitle="New Arrivals"/>
                </div>

                {/* Item Showcase */}
                <Divider />
                <div className="Product-Carousel">
                    <ProductCarousel bannerTitle="Top Picks for You"/>
                </div>


                {/* Advert Banner */}
                <Divider />
                <div className="Advert-Banner">
                    <AdvertBanner children="https://via.placeholder.com/728x90"/>
                </div>

                {/* Triple Card Links */}
                <Divider />
                <div className="Triple-Card">
                    <TripleCard/>


                </div>

                {/* Mailing List */}

            </div>
        </Page>
     );
}

export default Home;