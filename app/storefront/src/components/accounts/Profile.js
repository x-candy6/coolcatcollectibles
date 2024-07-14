import { AuthContext } from "./AuthContext";
import { useContext } from "react";
import Card from "../global/Card";

function Profile() {
    const { user } = useContext(AuthContext);
    return ( 
        <Card>
            <p>This is the profile for: {user.username}.</p>
        </Card>
     );
}

export default Profile;