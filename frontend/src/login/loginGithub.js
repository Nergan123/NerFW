function LoginGithub({additionalData}) {

  async function handleLogin() {
    let codeUrl = "https://github.com/login/oauth/authorize?scope=user,repo";        
    codeUrl += "&client_id=" + additionalData.clientId;
    window.location.replace(codeUrl);
  }

  return (
    <div>
      <button onClick={handleLogin}>
        Login with Github
      </button>
    </div>
  );
}


export default LoginGithub;