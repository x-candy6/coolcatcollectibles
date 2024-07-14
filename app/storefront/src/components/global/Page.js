import { AuthContext } from "../accounts/AuthContext";
import { useContext, useEffect } from "react";
import API from "../api/API";

function Page({ children }) {
    const { setUser } = useContext(AuthContext);

    useEffect(() => {
        const fetchSessionData = async () => {
            const access_token = localStorage.getItem('session-access-token');
            const refresh_token = localStorage.getItem('session-refresh-token');
            console.log(`Current Visitor\naccess_token: ${access_token}\nRefresh token: ${refresh_token}`);

            const headers = {
                'session-access-token': access_token,
                'session-refresh-token': refresh_token
            };
            try {
                if (access_token) {
                    // Validate the token -> GET validate_session_token
                    console.log("1")
                    const token_response = await fetchSessionToken(headers);
                    console.log("2", token_response.status)

                    if (token_response.status === 401) { // Expired session token -> refresh_session_token
                        console.log("3")
                        const response = await API.getReqWithHeaders(`/user/api/session/refresh_token/`, headers);
                        localStorage.setItem('session-access-token', response['access_token']);
                        localStorage.setItem('session-refresh-token', response['refresh_token']);

                        console.log(`Expired session token\nNew access_token: ${response.data.access_token}\nNew Refresh token: ${response.data.refresh_token}`);
                        console.log("4")
                    } else if (token_response.status === 404 || token_response.status === 400) { // No or invalid session token -> issue_guest_token
                        console.log("5")
                        const response = await API.getData(`/user/api/session/issue_token/`);

                        localStorage.setItem('session-access-token', response['access_token']);
                        localStorage.setItem('session-refresh-token', response['refresh_token']);
                        
                        // localStorage.setItem('access_token', response.data.access_token);
                        // localStorage.setItem('refresh_token', response.data.refresh_token);
                        console.log(`No or Invalid session token\nNew access_token: ${response['access_token']}\nNew Refresh token: ${response['refresh_token']}`);
                        console.log("6")
                    } else if (token_response.status === 200) { // Valid session token -> proceed
                        console.log("7")
                        console.log(`Access token is valid\nAccess Token: ${access_token}\nRefresh: ${refresh_token}`);
                    }
                } else { // New visitor
                    // issue_guest_token
                    console.log("8")
                    const response = await API.getData(`/user/api/session/issue_token/`);

                    localStorage.setItem('session-access-token', response['access_token']);
                    localStorage.setItem('session-refresh-token', response['refresh_token']);

                    // localStorage.setItem('access_token', response.data.access_token);
                    // localStorage.setItem('refresh_token', response.data.refresh_token);
                    console.log(`New Visitor\nNew access_token: ${response.data.access_token}\nNew Refresh token: ${response.data.refresh_token}`);
                }
                console.log("Valid Token")
            } catch (error) {
                console.log("Error fetching session tokens", error)
            }
        };

        fetchSessionData();
    }, []);

    const fetchSessionToken = async (headers) => {
        try {
            console.log(headers)
            const response = await API.getReqWithHeaders(`/user/api/session/validate_token/`, headers);
            console.log("THIS IS THE RESPONSE FROM FST", response)
            return response;
        } catch (error) {
            console.error('Error fetching session token:', error);
            if (error.response){
                return error.response;
            } else { 
                throw error;
            }
        }
    };

    return (
        <>
            <div className="page">
                {children}
            </div>
        </>
    );
}

export default Page;
