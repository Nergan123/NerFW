import "./loginGithub.css"
import GitHubLogo from "./github-mark-white.svg"


function LoginGithub({additionalData}) {

  async function handleLogin() {
    let codeUrl = "https://github.com/login/oauth/authorize?scope=user,repo";        
    codeUrl += "&client_id=" + additionalData.clientId;
    window.location.replace(codeUrl);
  }

  return (
    <div className="outterWrapper">
      <div className="innerWrapper">
        <img src={GitHubLogo} alt="GitHub Logo"/>
        <button onClick={handleLogin} className="button-Github">
          Login with Github
        </button>
      </div>
    </div>
  );
}


export default LoginGithub;