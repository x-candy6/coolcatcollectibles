import Card from "../global/Card";
import Grid from "../global/Grid";
import GridButton from "../global/GridButton";
import { Link } from "react-router-dom";

function Analytics() {
    return ( 
        
        <>
        <Card>
            Analytics Dashboard
            <Grid>
                <Link>
                    <GridButton>

                    </GridButton>
                </Link>
            </Grid>
        </Card>
        </>

     );
}

export default Analytics;