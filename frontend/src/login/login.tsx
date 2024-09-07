import Button from "../utils/button";
import React, {useContext, useState} from "react";
import {LoginResponse} from "@types";
import {Cookies} from "react-cookie";
import {useNavigate} from "react-router-dom";
import Popup from "./popup";
import A from "../utils/a";
import {BackgroundContext} from "../utils/backgroundProvider";
import Input from "../utils/input";

function Login() {

    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [popup, setPopup] = useState<boolean>(false);
    const [popupMessage, setPopupMessage] = useState<string>("");
    const background = useContext<string>(BackgroundContext);

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

    console.log(background);

    const style = {
        backgroundImage: `url(${background})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat"
    }

    return (
        <div style={style}
             className={"flex flex-col w-screen h-screen justify-center items-center bg-gradient-to-br from-main to-secondary"}>
            {popup && <Popup setPopup={setPopup} popupMessage={popupMessage} />}
            <div
                className={"flex flex-col p-5 border-2 border-white border-opacity-55 bg-opacity-5 bg-white backdrop-blur-lg rounded-2xl items-center gap-3"}>
                <h1 className={"text-4xl font-bold text-center text-white mb-3"}>Login</h1>
                <Input
                    placeholder={"Username"}
                    onChange={handleUsernameChange}
                />
                <Input
                    placeholder={"Password"}
                    type={"password"}
                    onChange={handlePasswordChange}
                />
                <Button className={"w-full"} onClick={handleLogin}>Login</Button>
                <A onClick={() => navigate("/Register")}>Don't have an account?</A>
            </div>
        </div>
    );
}

export default Login;
