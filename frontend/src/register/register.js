import React from "react";


function Register() {

    const [login, setLogin] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [passwordRepeat, setPasswordRepeat] = React.useState('');
  
    const handleLogin = (event) => {
      setLogin(event.target.value);
    };
  
    const handlePassword = (event) => {
      setPassword(event.target.value);
    };

    const handlePasswordRepeat = (event) => {
        setPasswordRepeat(event.target.value);
      };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const response = await fetch('/login/register', {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                "Login": login,
                "Password": password,
                "Repeat_password": passwordRepeat,
            })
           });

           if (response.redirected){
            window.location.href = response.url;
           }
    }

    return (
        <div id="register_menu" class="login-wrapper">
            <form onSubmit={handleSubmit}>
                <input type="text"
                    id="Login"
                    name="Login"
                    required=""
                    minlength="4"
                    maxlength="20"
                    size="20"
                    placeholder="Login"
                    style={{margin: "0 0 5%"}}
                    value={login}
                    onChange={handleLogin}
                />
                <input type="text"
                    id="Password"
                    name="Password"
                    required="" minlength="4"
                    maxlength="20"
                    size="20"
                    placeholder="Password"
                    style={{margin: "0 0 5%"}}
                    value={password}
                    onChange={handlePassword}
                />
                <input type="text"
                    id="Repeat_password"
                    name="Repeat_password"
                    required=""
                    minlength="4"
                    maxlength="20"
                    size="20"
                    placeholder="Repeat Password"
                    style={{margin: "0 0 5%"}}
                    value={passwordRepeat}
                    onChange={handlePasswordRepeat}
                />
                <input type="submit" id="Submit" name="Submit" size="20" value="Submit" />
            </form>
        </div>
    );
}


export default Register;