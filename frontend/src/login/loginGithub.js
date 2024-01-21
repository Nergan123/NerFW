import { useState } from "react";


function LoginGithub({additionalData}) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleLogin() {
    
  }

  return (
    <div>
      <button onClick={handleLogin}>
        Login with Github
      </button>
      <p>{additionalData.clientId}</p>
    </div>
  );
}


export default LoginGithub;