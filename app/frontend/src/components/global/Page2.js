//This page doesn't have a useEffect to check authentication, it's used for Login.js so that theres only 1 call to the API


function Page2({children}) {



    return ( 
        <div class=" rounded-lg m-10 h-full page">
            <p>hello</p>
            {children}
        </div>


     );
}

export default Page2;