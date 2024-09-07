import React, {useContext, useState} from "react";
import {BackgroundContext} from "../utils/backgroundProvider";
import Button from "../utils/button";
import Input from "../utils/input";
import A from "../utils/a";
import {useNavigate} from "react-router-dom";

function Register() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirm, setPasswordConfirm] = useState("");
    const [email, setEmail] = useState("");

    const background = useContext<string>(BackgroundContext);
    const navigate = useNavigate();

    const style = {
        backgroundImage: `url(${background})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat"
    }

    function handleUsernameChange(event: React.ChangeEvent<HTMLInputElement>) {
        setUsername(event.target.value);
    }

    function handlePasswordChange(event: React.ChangeEvent<HTMLInputElement>) {
        setPassword(event.target.value);
    }

    function handlePasswordConfirmChange(event: React.ChangeEvent<HTMLInputElement>) {
        setPasswordConfirm(event.target.value);
    }

    function handleEmailChange(event: React.ChangeEvent<HTMLInputElement>) {
        setEmail(event.target.value);
    }

    function handleRegister() {
        console.log("Registering...");
    }

    return (
        <div style={style} className={"flex flex-col w-screen h-screen justify-center items-center"}>
            <div
                className={"flex flex-col p-5 lg:w-[30rem] border-2 border-white border-opacity-55 bg-opacity-5 bg-white backdrop-blur-lg rounded-2xl items-center gap-3"}>
                <h1 className={"font-bold text-white text-2xl mb-5"}>Register</h1>
                <Input
                    placeholder={"Username"}
                    onChange={handleUsernameChange}
                />
                <Input
                    placeholder={"Email"}
                    onChange={handleEmailChange}
                />
                <Input
                    placeholder={"Password"}
                    type={"password"}
                    onChange={handlePasswordChange}
                />
                <Input
                    placeholder={"Confirm Password"}
                    type={"password"}
                    onChange={handlePasswordConfirmChange}
                />
                <A onClick={() => navigate("/Login")}>Have an account?</A>
                <Button onClick={handleRegister}>Register</Button>
            </div>
        </div>
    );
}

export default Register;
