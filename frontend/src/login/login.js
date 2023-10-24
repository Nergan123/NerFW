import React from "react";
import './login.css'


function Login() {
    return (
        <div id="login_menu" className="login-wrapper">
            <form method="POST">
                <input type="text" id="Login" name="Login" required="" minLength="4" maxLength="20" size="20" style={{margin: "0 0 5%"}} placeholder="Login" />
                <input type="text" id="Password" name="Password" required="" minLength="4" maxLength="20" size="20" style={{margin: "0 0 5%"}} placeholder="Password" />
                <input type="submit" id="Submit" name="Submit" size="20" value="Submit" style={{margin: "0 0 5%"}} />
            </form>
        </div>
    );
}


export default Login;