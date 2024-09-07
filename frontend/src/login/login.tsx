import Button from "../utils/button";
import React, {useEffect, useState} from "react";
import {LoginResponse} from "@types";
import {Cookies} from "react-cookie";
import {useNavigate} from "react-router-dom";
import Popup from "./popup";

function Login() {

    const [backgroundImage, setBackgroundImage] = useState<string>("");
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [popup, setPopup] = useState<boolean>(false);
    const [popupMessage, setPopupMessage] = useState<string>("");

    const cookie = new Cookies();
    const navigate = useNavigate();

    function handleUsernameChange(event: React.ChangeEvent<HTMLInputElement>) {
        setUsername(event.target.value);
    }

    function handlePasswordChange(event: React.ChangeEvent<HTMLInputElement>) {
        setPassword(event.target.value);
    }

    async function handleLogin() {
        const response = await fetch("/api/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const body: LoginResponse = await response.json();
        if (body.success) {
            cookie.set("token", body.token);
            navigate("/")
        } else {
            setPopupMessage(body.message);
            setPopup(true);
        }
    }

    const style = {
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat"
    }

    useEffect(() => {
        async function fetchBackground() {
            try {
                const response = await fetch("/api/ui/background");
                const blob = await response.blob();
                const url = URL.createObjectURL(blob);
                setBackgroundImage(url);
            } catch (error) {
                console.error("Error fetching background image:", error);
            }
        }

        fetchBackground().then();
    }, []);

    return (
        <div style={style}
             className={"flex flex-col w-screen h-screen justify-center items-center bg-gradient-to-br from-main to-secondary"}>
            {popup && <Popup setPopup={setPopup} popupMessage={popupMessage} />}
            <div
                className={"flex flex-col p-5 border-2 border-white border-opacity-55 bg-opacity-5 bg-white backdrop-blur-lg rounded-2xl items-center gap-3"}>
                <h1 className={"text-4xl font-bold text-center text-white mb-3"}>Login</h1>
                <input
                    className={"p-2 rounded bg-opacity-5 bg-white border-1 border-white text-white hover:bg-opacity-20 transition-all ease-in-out duration-300"}
                    placeholder={"Username"}
                    onChange={handleUsernameChange}
                />
                <input
                    className={"p-2 rounded bg-opacity-5 bg-white border-1 border-white text-white hover:bg-opacity-20 transition-all ease-in-out duration-300"}
                    placeholder={"Password"}
                    type={"password"}
                    onChange={handlePasswordChange}
                />
                <Button className={"w-full"} onClick={handleLogin}>Login</Button>
            </div>
        </div>
    );
}

export default Login;
