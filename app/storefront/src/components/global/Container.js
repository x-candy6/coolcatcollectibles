import Page from "./Page";

function Container({children}) {
    return ( 
        <Page>
            <div class="h-full container">

                <div class="container-left">

                </div>

                <div class="rounded-lg  container-mid">
                    {children}
                </div>

                <div class="container-right">

                </div>

            </div>
        </Page>


     );
}

export default Container;