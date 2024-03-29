import PatreonLogo from "./PATREON_SYMBOL_1_WHITE_RGB.svg"
import "./loginPatreon.css"

function LoginPatreon({additionalData}) {

  async function handleLogin() {
    let codeUrl = "https://patreon.com/oauth2/authorize?response_type=code";        
    codeUrl += "&client_id=" + additionalData.clientId;
    codeUrl += "&redirect_uri=" + additionalData.redirectUrl;
    codeUrl += "&scope=identity";
    window.location.replace(codeUrl);
  }

  return (
    <div className="outterWrapper">
      <div className="innerWrapper">
        <img src={PatreonLogo} alt="Patreon Logo"/>
        <button onClick={handleLogin} className="button-Patreon">
          Login with Patreon
        </button>
        </div>
    </div>
  );
}


export default LoginPatreon;