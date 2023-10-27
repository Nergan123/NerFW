import React from "react";
import './login.css'


function Login() {

    const [login, setLogin] = React.useState('');
    const [password, setPassword] = React.useState('');

    const handleLogin = (event) => {
      setLogin(event.target.value);
    };
  
    const handlePassword = (event) => {
      setPassword(event.target.value);
    };
  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      const response = await fetch('/login', {
        method: 'POST',
        redirect: 'follow',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({
            "Login": login,
            "Password": password,
        })
       });

       if (response.redirected){
            window.location.href = response.url;
       }
    };

    return (
        <div id="login_menu" className="login-wrapper">
            <form onSubmit={handleSubmit}>
                <input type="text" id="Login" name="Login" required="" minLength="4" maxLength="20" size="20" style={{margin: "0 0 5%"}} placeholder="Login" value={login} onChange={handleLogin} />
                <input type="text" id="Password" name="Password" required="" minLength="4" maxLength="20" size="20" style={{margin: "0 0 5%"}} placeholder="Password" value={password} onChange={handlePassword} />
                <input type="submit" id="Submit" name="Submit" size="20" value="Submit" style={{margin: "0 0 5%"}} />
            </form>
        </div>
    );
}


export default Login;