

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
        <button onClick={handleLogin} className="button-Patreon">
          Login with Patreon
        </button>
        </div>
    </div>
  );
}


export default LoginPatreon;