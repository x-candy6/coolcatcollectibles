import Card from "../global/Card";
import Grid from "../global/Grid";
import GridButton from "../global/GridButton";
import { Link } from "react-router-dom";

function Storefronts() {
    return ( 
        <>
        <Card>
            Storefronts Dashboard
            <Grid>
                <Link to="/coolcatcollectiblesshop">
                    <GridButton>
                        coolcatcollectibles.shop
                    </GridButton>
                </Link>
            </Grid>
        </Card>
        </>

     );
}

export default Storefronts;