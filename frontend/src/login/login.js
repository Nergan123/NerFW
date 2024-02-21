import { useEffect } from 'react';
import { useState } from 'react';
import LoginDefault from './loginDefault.js';
import LoginGithub from './loginGithub.js';
import LoginPatreon from './loginPatreon.js';
import { useNavigate } from 'react-router-dom';
import {Cookies} from "react-cookie";


const LOGIN_METHOD_DEFAULT = 'default';
const LOGIN_METHOD_GITHUB = 'github';
const LOGIN_METHOD_PATREON = 'patreon';

function Login() {
    const [loginMethod, setLoginMethod] = useState(LOGIN_METHOD_DEFAULT);
    const [additionalData, setAdditionalData] = useState({});

    const navigate = useNavigate();
    const cookie = new Cookies();

    useEffect(() => {
        console.log("Fetching")
        const fetchLoginMethod = async () => {
            const response = await fetch('/login', {
                method: 'GET'
            });
    
            const data = await response.json();

            setAdditionalData(data.additionalData);
            setLoginMethod(data.method);
        }

        fetchLoginMethod();
    }, [setLoginMethod, setAdditionalData]);

    if (cookie.get("error")) {
        navigate("/Unauthenticated");
    }

    if (loginMethod === LOGIN_METHOD_GITHUB) {
        return <LoginGithub additionalData={additionalData} />;
    } else if (loginMethod === LOGIN_METHOD_PATREON) {
        return <LoginPatreon additionalData={additionalData} />;
    }
    
    return <LoginDefault />;
}


export default Login;