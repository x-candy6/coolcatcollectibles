import Page from "../Page";

function TableContainer({children}) {
    return ( 
        <Page>
            <div class="h-full w-full TableContainer">

                    {children}

            </div>
        </Page>


     );
}

export default TableContainer;