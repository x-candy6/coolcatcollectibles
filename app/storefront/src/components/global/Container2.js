import Page2 from "./Page2";

function Container2({children}) {
    return ( 
        <Page2>
            <div class="h-full container">

                <div class="container-left">

                </div>

                <div class="rounded-lg  container-mid">
                    {children}
                </div>

                <div class="container-right">

                </div>

            </div>
        </Page2>


     );
}

export default Container2;