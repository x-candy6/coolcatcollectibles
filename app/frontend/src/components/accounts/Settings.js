import { useContext } from "react";
import { AuthContext } from "./AuthContext";
import Card from "../global/Card";



function Settings() {
  const { user } = useContext(AuthContext);



  return (
    <Card>
      <p>This is the settings for: .</p>
    </Card>
  );
}


export default Settings;