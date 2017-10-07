import Request from "es6-request";
import UserTokenStorage from "./UserTokenStorage";


const BACKEND_URL = "http://localhost:8990";


export default class Authenticator {

    /**
     * Logs in to the backend and returns an authentication token
     *
     * @returns {string}
     */
    static login(username, password) {
        return new Promise(function(resolve, reject) {
            Request.post(BACKEND_URL + "/auth/login/")
                .sendJSON({
                    'username': username,
                    'password': password,
                })
                .then((result) => {
                    const [body, response] = result;
                    let bodyJson;

                    if(response.statusCode !== 200) {
                        reject(body);
                    }

                    try {
                        bodyJson = JSON.parse(body);
                    } catch (e) {
                        reject(e.message);
                    }

                    resolve(bodyJson.token);
                });
        });
    }


    /**
     * Logs out to the backend and returns True if successful
     *
     * @returns {bool}
     */
    static logout() {
        UserTokenStorage.deauthenticateUser();
        return true;
    }
}