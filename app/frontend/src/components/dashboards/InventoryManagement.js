import Card from "../global/Card";
import Grid from "../global/Grid";
import GridButton from "../global/GridButton";
import { Link } from "react-router-dom";


function InventoryManagement() {
    return ( 
        <>
            <Card>
                <h1>Inventory Management</h1>
                <Grid>
                <Link to="/general-inventory">
                    <GridButton>
                        General Inventory
                    </GridButton>
                </Link>

                <Link>
                    <GridButton>
                        eBay Inventory
                    </GridButton>
                </Link>

                <Link>
                    <GridButton>
                        TikTok Inventory
                    </GridButton>
                </Link>

                <Link>
                    <GridButton>
                        General Configuration
                    </GridButton>
                </Link>

                <Link>
                    <GridButton>
                        eBay Configuration
                    </GridButton>
                </Link>

                <Link>
                    <GridButton>
                        TikTok Configuration
                    </GridButton>
                </Link>
                </Grid>


            </Card>
        </>
     );
}

export default InventoryManagement;