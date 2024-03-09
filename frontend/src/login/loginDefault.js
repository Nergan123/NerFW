import { useState } from "react";
import { useNavigate } from "react-router-dom";
import './login.css'


function LoginDefault() {

    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = (event) => {
      setLogin(event.target.value);
    };
  
    const handlePassword = (event) => {
      setPassword(event.target.value);
    };
  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      const response = await fetch('/api/authorize', {
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

       if(response.status === 200){
          navigate("/");
       }else if(response.status === 401) {
          alert("This Login is not authorized on this website.");
       }else{
          navigate("/register");
       };
    };

    return (
        <div id="login_menu" className="login-wrapper">
            <form onSubmit={handleSubmit}>
                <input type="text" id="Login" name="Login" required="" minLength="4" maxLength="20" size="20" style={{margin: "0 0 5%"}} placeholder="Login" value={login} onChange={handleLogin} />
                <input type="password" id="Password" name="Password" required="" minLength="4" maxLength="20" size="20" style={{margin: "0 0 5%"}} placeholder="Password" value={password} onChange={handlePassword} />
                <input type="submit" id="Submit" name="Submit" size="20" value="Submit" style={{margin: "0 0 5%"}} />
            </form>
        </div>
    );
}


export default LoginDefault;